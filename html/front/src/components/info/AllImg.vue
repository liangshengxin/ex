<template>
<!-- 图集 -->
<!-- 图片大小 width:110px; height:84px; -->

<div class="all-img info-border">
    <!-- 头像 标题 类型 -->
    <div class="up-all">
        <!-- 头像标题 -->
        <div class="up-all-left">
            <!-- 头像 -->
            <div class="up-all-left-img">
                <img v-lazy="infos.headimg" />
            </div>
            <!-- 标题 -->
            <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="span">
                {{infos.title}}
            </router-link>
        </div>
        <!-- 类型 -->
        <div class="up-all-right">
            <div>{{infos.type}}</div>
        </div>
    </div>
    <!-- 图集 -->
    <div class="down-all">
        <div class="down-all-img" v-for="(imglist, key) in infos.imageAll" :key="key">
            <div v-for="(item, index) in imglist" :key="index">
                <img v-lazy="{src:item}" />
            </div>
        </div>
    </div>
</div>
</template>


<script>
// 数据格式
// infos:{
//     headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a4.png',
//     imageAll:[
//         [
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w1.jpg',
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w2.jpg',
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w3.jpg',
//         ],
//         [
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w4.jpg',
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w5.jpg',
//             'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/w6.jpg',
//         ],
//     ],
//     type:'图集',
//     title:'诺奖得主回忆通知获奖那一刻',
// }
export default {
    name:'infoAllImg',
    props:{
        infos:Object
    }
}
</script>


<style scoped>
.all-img{
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
/* 头像标题 */
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
/* 标题 */
.up-all-left>span{
    font-size:18px;
    font-weight:bold;
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

/* 图集 */
.down-all-img{
    display: flex;
    justify-content:space-between;
    padding-top:5px;
}
.down-all-img>div{
    width:110px;
    height:84px;
    overflow: hidden;
}
.down-all-img>div>img{
    width:100%;
}
</style>
