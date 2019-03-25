<template>
<div class="no-img info-border">
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

        <!-- 简介 -->
        <div class="in-synopsis no-ellipsis">{{infos.synopsis}}</div>
    </router-link>
   

</div>
</template>

<script>
// 数据格式
// infos:{
//     headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a4.png',
//     name:'大兔',
//     type:'趣问',
//     title:'“你的旅行，是什么颜色？” 晒照片，换北欧梦幻极光之旅！',
//     synopsis:'狗狗狗狗会天天的跟着我们生活在一起，它们的一切都会影响着主人，尤其是狗狗身上散发的味道，会无时无刻的'
// }
export default {
    name:'infoNoImg',
    props:{
        infos:Object
    }
}
</script>


<style scoped>
.no-img{
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
</style>
