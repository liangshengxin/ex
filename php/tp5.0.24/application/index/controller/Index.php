<?php
namespace app\index\controller;

use app\index\model\ArticleSync;
use mongodb\Client;
use redis\Client as RedisClient;
use think\Db;

class Index
{
    public function index()
    {
        echo "<pre/>";
        $ar = new ArticleSync();
        // $ar->mongoDBTab="csdn.article";
        // dump($ar->syncMongoMysql());
        dump($ar->getSyncRedis());
    }

}
