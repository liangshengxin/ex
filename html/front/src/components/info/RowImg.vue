<template>
<!-- 横排多图信息 -->
<!-- 图片大小 width:110px; height:84px; -->
<div class="row-img info-border">
    <!-- 头像 名称 类型 -->
    <div class="row-own">
        <!-- 头像名称 -->
        <div class="row-all">
            <!-- 头像 -->
            <div class="row-all-img">
                <img :src="infos.headimg" />
            </div>
            <!-- 名称 -->
            <span class="row-nowrap">{{infos.name}}</span>
        </div>
        <!-- 类型 -->
        <div class="row-type row-nowrap">
            <div>{{infos.type}}</div>
        </div>
    </div>

    <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="div">
        <!-- 标题 -->
        <div class="row-title row-ellipsis"><h3>{{infos.title}}</h3></div>

        <!-- 图片 -->
        <div class="row-image">
            <div v-for="(item, index) in infos.image_list" :key="index">
                <img v-lazy="item" />
            </div>
        </div>

        <!-- 简介 -->
        <div class="row-synopsis row-ellipsis">{{infos.synopsis}}</div>
    </router-link>
   
</div>
</template>

<script>
// 数据格式
// infos:{
//     headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a3.png',
//     image_list:[
//         'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/qq1.jpg',
//         'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/qq2.jpg',
//         'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/qq3.jpg',
//     ],
//     name:'养了猫的飞飞',
//     type:'阅读',
//     title:'浣熊孤儿掉到树下，被一家人收养之后……',
//     synopsis:'巴哈马拿骚的居民Rosie Kemp发现一个刚出生的浣熊，掉在了树下。因为找不到小浣熊的妈妈了，Rosie和她的女儿Laura Young决定收养这只小东西，并给她取名“小南瓜”。'
// }
export default {
    name:'infoRowImg',
    props:{
        infos:Object
    }
}
</script>

<style scoped>
.row-img{
    margin:0 15px;
    text-align:left;
    padding-bottom:18px;
}
.row-own{
    display: flex;
    justify-content:space-between;
}
/* 头像 名称 */
.row-all{
    display:flex;
    align-items:center;
    height:50px;
}
/* 头像 */
.row-all-img{
    width:30px;
    height:30px;
    border-radius:20px;
    overflow:hidden;
}
.row-all-img>img{
    width:100%;
}
/* 名称 */
.row-all>span{
    font-size:14px;
    color:#757575;
    padding-left:8px;

    width:200px;
}
/* 类别 */
.row-type{
    display:flex;
    align-items:center;
    justify-content:flex-end;
    font-size:14px;
    color:#fe9700;
    height:50px;
    width: 105px;
}
.row-type>div{
    border-right:2px solid #fe9700;
    padding-right:5px;
    height:20px;
    line-height:20px;
}

/* 标题 */
.row-title>h3{
    font-size:18px;
    line-height: 1.4;
    font-weight:bold;
    overflow:hidden; 
}
/* 简介 */
.row-synopsis{
    padding-top:5px;
    color:#757575;
    font-size:14px;
    line-height: 1.4;
    overflow:hidden; 
}
/* 图片 */
.row-image{
    display: flex;
    justify-content:space-between;
    padding-top:5px;
}
.row-image>div{
    width:110px;
    height:84px;
    overflow: hidden;
}
.row-image>div>img{
    width:100%;
}


.row-ellipsis{
    text-overflow:ellipsis;
    display:-webkit-box; 
    -webkit-box-orient:vertical;
    -webkit-line-clamp:2;
}
/* 超出隐藏 */
.info-nowrap{
    overflow: hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}
</style>
