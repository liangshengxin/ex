<template>
<!-- 单张大图 -->
<!-- 图片大小 width: 340px; height:140px; -->
<div class="max-img info-border">
    <!-- 头像名称类别 -->
    <div class="up-all">
        <!-- 头像名称 -->
        <div class="up-all-left">
            <!-- 头像 -->
            <div class="up-all-left-img">
                <img v-lazy="infos.headimg" />
            </div>
            <!-- 名称 -->
            <span>{{infos.name}}</span>
        </div>
        <!-- 类型 -->
        <div class="up-all-right">
            <div>{{infos.type}}</div>
        </div>
    </div>

    <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="div">
        <!-- 标题 -->
        <div class="in-title ">{{infos.title}}</div>

        <!-- 大图 -->
        <div class="in-image">
            <div class="in-image-center">
                <img v-lazy="{src:infos.image}"/>
            </div>
        </div>

        <!-- 简介 -->
        <div class="in-synopsis no-ellipsis">{{infos.synopsis}}</div>
    </router-link>
    
</div>
</template>

<script>
// 数据格式
/**
    infos:{
        headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a5.png',
        image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/c1.png',
        name:'Hope',
        type:'专题',
        title:'心情不好了，就来看看这只狗！',
        synopsis:'猫咪不像人，猫咪的情绪不会写在脸上，反馈给我们的信息更多的应该是行为上肢体上的，当然从叫声中也会'
    }
 */
export default {
    name:'infoMaxImg',
    props:{
        infos:Object
    }
}
</script>

<style scoped>
.max-img{
    margin:0 15px;
    text-align:left;
    padding-bottom:18px;
}
/* 头像名称类型 */
.up-all{
    display:flex;
    align-items:center;
    justify-content:space-between;
    height:50px;
}
/* 头像名称 */
.up-all-left{
    display:flex;
    align-items:center;
}
/* 头像 */
.up-all-left-img{
    width:30px;
    height:30px;
    border-radius:20px;
    overflow:hidden;
}
.up-all-left-img>img{
    width:100%;
}
/* 名称 */
.up-all-left>span{
    font-size:14px;
    padding-left:8px;
}
/* 类别 */
.up-all-right{
    font-size:14px;
    color:#fe9700;
}
.up-all-right>div{
    border-right:2px solid #fe9700;
    padding-right:5px;
    height:20px;
    line-height:20px;
}

/* 标题 */
.in-title{
    font-size:18px;
    line-height: 1.4;
    font-weight:bold;
}
.in-synopsis{
    padding-top:5px;
    color:#757575;
    font-size:14px;
    line-height: 1.4;
}
/* 超出隐藏 */
.no-ellipsis{
    text-overflow:ellipsis;
    display:-webkit-box; 
    -webkit-box-orient:vertical;
    -webkit-line-clamp:2;
    overflow: hidden;
}
/* 大图 */
.in-image{
    display: flex;
    justify-content: center;
    overflow: hidden;

}
.in-image-center{
    width: 340px;
    height:140px;
    padding-right:2px;
    padding-top:8px;
}
.in-image-center>img{
    width:100%;
}
</style>
