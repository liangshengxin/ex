<?php
/**
 * @info
 * @desc Created by PhpStorm.
 * @author: LiangShengXin
 * @QQ：738557220
 * @since: 2019/3/8 0:32
 */

namespace app\index\model;

use mongodb\Client;
use redis\Client as RClient;
use MongoDB\Driver;

use think\Model;


class ArticleSync extends Model{
    protected $table = 'article';
    protected $field = true;
    public $mongoDBTab = 'toutiao.article'; #mongodb数据库 表
    public $mongoDBExitCount = 50; //达到指定数量才能更新mongodb读取的数据

    const REDIS_HASH = 'article:hash:id:';  #资讯信息键名前缀 保存内容
    const REDIS_SET_GROUP = 'article:set:group:';  #分组键名前缀 保存为个组中分配的内容id 无内容前缀
    const REDIS_ZSET = 'article:zset:groups'; #总组 保存各组的键名id 不含前缀
    const REDIS_TIME = 3600*24*3; #数据有效时间 s
    

    /**
     * 获取未读数据游标
     * @param int $limit 数据最大数量
     * @param int $day  查询哪天 0当天 -1上一天 1下一天
     * @return bool|\MongoDB\Driver\Cursor
     */
    private function getDBCursor($limit=100,$day=0){
        $date = date('Y-m-d',strtotime("{$day} day"));
        $filter = [
            'data_format'=>$date,
            'is_read'=>null, #未读游标
        ];
        $options = [
            'sort'=>[
                'time_format'=>-1
            ],
            'limit'=>$limit,
        ];
        $query = new Driver\Query($filter,$options);
        $cursor = Client::connect()->executeQuery($this->mongoDBTab,$query);
        return $cursor;
    }


    /**
     * 读取游标 并将读取数据标记为已读
     * @param Driver\Cursor $cursor 数据游标
     * @return bool|object data数组数据 count读取更新个数
     */
    private function updateDBWrite(Driver\Cursor $cursor){
        $data = [];
        $bulk = new Driver\BulkWrite();
        foreach($cursor as $item){
            $item = (array)$item;
            $_id = array_shift($item);
            $bulk->update(['_id'=>$_id],['$set'=>['is_read'=>'1']]);
            $data[] = $item;
        }
        if(!$data) return false; #数据为空
        if(count($data)<$this->mongoDBExitCount) return false; #数据数量过少

        $result = Client::connect()->executeBulkWrite($this->mongoDBTab,$bulk);
        return (object)['data'=>$data,'count'=>$result->getModifiedCount()];
    }


    /**
     * 数据同步 mongodb -> mysql
     * countMax 同步个数
     * @return string 同步数量 同步时间
     */
    public function syncMongoMysql($countMax=100){
        $day = 0; #天数 当天
        $dayEnd = -5; #向前查询天数
        $dataObj = null;
        do{
            $cursor=$this->getDBCursor($countMax,$day);
            $dataObj = $this->updateDBWrite($cursor);
            $day--;
        }while(!$dataObj && $day>$dayEnd);

        if(!$dataObj) return json_encode(["code"=>0,"msg"=>"空"],JSON_UNESCAPED_UNICODE); 

        $data = $this->saveAll($dataObj->data);
        $msg = array_merge(
            ['count'=>count($data)],
            ['add_time'=>date('Y-m-d H:i:s',time())]
        );
        return json_encode($msg,JSON_UNESCAPED_UNICODE);
    }

    /**
     * 读取mysql数据 并将数据设为以读
     * @param int $limit 读取个数
     * @return object count个数  data数组
     */
    private function updateMysqlWrite($limit=100){
        $data = [];
        // 读取
        $readData = $this->where(['is_read'=>'1'])->whereOr(['is_read'=>null])
            ->order('id','desc')
            ->limit($limit)
            ->select();

        //更新
        $updateData = [];
        foreach($readData as $item){
            $updateData[]=[
                'id'=>$item->id,
                'is_read'=>2,
            ];
            $data[] = $item->toArray();
        }
        
        $count = $this->saveAll($updateData); #更新的数据
        return (object)['count'=>count($count),'data'=>$data];
    }


    /**
     * 数据存入redis （打乱数组）
     * @param $data array 二维信息数组
     * @return int|\Redis|string 存入的数量 | 连接失败信息
     */
    private function setRedis($data){
        // 连接
        $redis = RClient::connect();
        if(is_string($redis)) return $redis;
        $sumArticle = 0;

        shuffle($data);
        
        // 分组
        $groupData = array_chunk($data,10);

        foreach($groupData as $k=>$items){
            $groupK = time()+$k;
            $setGroupKey = self::REDIS_SET_GROUP.$groupK; #分组键名

            foreach($items as $item){
                $hashKey = self::REDIS_HASH.$item['id']; #内容键名
                $redis->hmset($hashKey,$item); #存储内容
                $redis->sadd($setGroupKey,$item['id']); #内容id存入分组
            }

            //分组id 存入总组 score=time+k
            $sumArticle += $redis->zadd(self::REDIS_ZSET,$groupK,$groupK);
        }
        return $sumArticle;
    }


    /**
     * 同步mysql -> redis
     * countMax 读取个数
     * @return int|\Redis|string
     */
    public function syncMysqlRedis($countMax=100){
        // 获取数据
        $dataObj = $this->updateMysqlWrite($countMax);
        $count = $this->setRedis($dataObj->data);
        if(is_string($count)) return $count;

        return json_encode([
            'count_group'=>$count,    #本次存入数量 几组
            'sum_group'=>RClient::connect()->zCard(self::REDIS_ZSET), #总数量 总组
            'get_count'=>$dataObj->count, #本次获取数量 个数
        ],JSON_UNESCAPED_UNICODE);
    }



    // 数据同步mongodb - mysql - redis
    public function syncCategory(){
        $this->mongoDBTab = "csdn.article"; //csdn数据
        $camm = $this->syncMongoMysql(50); //读取50个 存入mysql
        echo "<hr>csdn - mongodb - mysql :".$camm;

        $this->mongoDBTab = "toutiao.article"; //toutiao数据
        $tamm = $this->syncMongoMysql(50); //读取50个 存入mysql
        echo "<hr>toutiao - mongodb - mysql :".$tamm;

        $smre = $this->syncMysqlRedis(100); //从mysql中读取100个 并打乱 存入redis
        echo "<hr>mysql - redis:".$smre;
        
        return;
    }



    public function getSyncRedis($startPage=0,$endPage=0){
        $redis = RClient::connect();
        $zRevRange = $redis->zRevRange(self::REDIS_ZSET,$startPage,$endPage);
        $data = [];
        foreach($zRevRange as $id){
            foreach($redis->sMembers(self::REDIS_SET_GROUP.$id) as $keyId){
                $data[] = $redis->hGetAll(self::REDIS_HASH.$keyId);
            }
        }
        return $data;
    }
}