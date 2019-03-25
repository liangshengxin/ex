<template>
<!-- 单图信息 -->
<!-- 图片大小 width:110px; height:85px; -->
<div class="single info-border">
    <!-- 头像文字说明 -->
    <div class="info-title">

        <!-- 头像名称 -->
        <div class="img-name">
            <!-- 头像 -->
            <div class="img">
                <img v-lazy="infos.headimg" />
            </div>
            <!-- 名称 -->
            <span>{{infos.name}}</span>
        </div>

        <!-- 文字说明 -->
        <router-link :to="'/read/'+infos.id+'/'+infos.category" class="info-content" tag="div">
            <h3>{{infos.title}}</h3>
            <div class="content">{{infos.synopsis}}</div>
        </router-link>
        
    </div>


    <!-- 类别图片 -->
    <div class="type-img">
        <!-- 类别 -->
        <div class="down-type"> 
            <div>{{infos.type}}</div>
        </div>
        <!-- 图片 -->
        <router-link :to="'/read/'+infos.id+'/'+infos.category" class="down-img" tag="div">
            <img v-lazy="infos.image"/>
        </router-link>
    </div>
</div>
</template>

<script>
//数据格式
// infos:{
//     id:1,
//     category:1,//类别
//     headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a1.png',
//     image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/q1.jpg',
//     name:'Super invincible 菁',
//     type:'新鲜事',//类别名称
//     title:'十一长假哪也不去，宅在家里看电影！',
//     synopsis:'每总有人山人海，静静地呆在家，坐在电脑'
// }
export default {
    name:'infoSingleImg',
    props:{
        infos:Object
    }
    
}
</script>

<style scoped>
.single{
    margin:0 15px;
    display:flex;
    height:160px;
    text-align:left;
    justify-content:space-between;
    position: relative;
}

/* 头像文字说明 */
.info-title{
    display:flex;
    flex-direction:column;
    width:230px;
    overflow:hidden;
    /* white-space:nowrap; */
    /* text-overflow:ellipsis; */
    
}
/* 类别 图片 */
/* .type-img{
    flex-grow:2;
    background:#999;
} */


/* 头像名称 */
.img-name{
    display:flex;
    align-items:center;
    height:50px;
    /* flex:1 auto; */
}
/* 头像 */
.img{
    width:30px;
    height:30px;
    border-radius:20px;
    overflow:hidden;
}
.img>img{
    width:100%;
}
/* 名称 */
.img-name>span{
    font-size:14px;
    color:#757575;
    padding-left:8px;
}

/* 文字 说明 */
.info-content{
    text-overflow:ellipsis;
    display:-webkit-box; 
    -webkit-box-orient:vertical;
    -webkit-line-clamp:2;
}
/* 标题 */
.info-content>h3{
    font-size:18px;
    line-height: 1.4;
    font-weight:bold;
    overflow:hidden; 
}
/* 简介 */
.content{
    padding-top:5px;
    color:#757575;
    font-size:14px;
    line-height: 1.4;
    overflow:hidden; 
}
/* 类别 */
.down-type{
    display:flex;
    align-items:center;
    justify-content:flex-end;
    font-size:14px;
    color:#fe9700;
    height:50px;
}
.down-type>div{
    border-right:2px solid #fe9700;
    padding-right:5px;
    height:20px;
    line-height:20px;
}
/* 图片 */
.down-img{
    width:110px;
    height:85px;
    overflow:hidden;
}
.down-img>img{
    width:100%;
}
</style>