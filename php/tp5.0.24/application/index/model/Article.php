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


class Article{
    static public function getList($limit=100,$day=0){
       $date = date('Y-m-d',strtotime("{$day} day"));
       $filter = [
           // 'date_format'=>$date
       ];
       $options = [
           'maxTimeMS' => 1000,
           'sort'=>[
            //    'time_format'=>-1
                'date_format'=>-1
           ],
           'limit'=>$limit,
       ];
       $query = new \MongoDB\Driver\Query($filter,$options);
       $cursor = Client::connect()->executeQuery('toutiao.article',$query);
       if(iterator_count($cursor)<=0) return false; #无数据
       return $cursor->toArray();
    }
    static public 
    public function sync(){

    }
}