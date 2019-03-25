<template>
<!-- 带文字大图信息 -->
<!-- 图片大小 width: 340px; height:110px; -->
<div class="text-img info-border">

    <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="div">
        <!-- 图片 标题 -->
        <div class="up-all">
            <!-- 背景 -->
            <div class="up-all-background"></div>

            <!-- 图片 -->
            <div class="up-all-img"><img v-lazy="{src:infos.image}" /></div>

<!-- <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="div"> -->
            <!-- 标题 -->
            <div class="up-all-title">{{infos.title}}</div>
<!-- </router-link> -->
            
        </div>
    </router-link>
    
    
    <!-- 头像 名称 -->
    <div class="in-all">
        <div class="in-all-headimg">
            <img v-lazy="infos.headimg" />
        </div>
        <span class="in-all-name">{{infos.name}}</span>
    </div>

    <!-- 简介 -->
    <router-link :to="'/read/'+infos.id+'/'+infos.category" tag="div">
        <div class="down-all text-ellipsis">{{infos.synopsis}}</div>
    </router-link>

</div>
</template>

<script>
// 数据格式
/**
   infos:{
        image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/c2.png',
        title:'一周在任意地点工作三天？',
        headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/c.png',
        name:'SeeYouAgain',
        synopsis:'这是一家帮助客户在亚太地区找到适合的打折酒店的中介机构，在全球设立了9个办事处，老板克里斯蒂安·米'
    }
 */
export default {
    name:'infoTextImg',
    props:{
        infos:Object
    }
}
</script>


<style scoped>
.text-img{
    margin:0 15px;
    text-align:left;
    padding-bottom:18px;
    padding-top:18px;
    position: relative;
}

/* 图片 标题 */

.up-all{
    height: 110px;
    overflow: hidden;
    position: relative;
}
/* 图片背景 */
.up-all-background{
    background-image: url(../../assets/background.png);
    background-size:340px 110px;
    background-repeat:no-repeat;
    width:340px;
    height: 110px;
    position: absolute;
    z-index: 2;
}
/* 图片 */
.up-all-img{
    width: 340px;
}
.up-all-img>img{
    width: 100%;
}
/* 标题 */
.up-all-title{
    position: absolute;
    bottom:10px;
    left:90px;
    font-size:18px;
    color:#fff;
    z-index: 9;
}

/* 头像 名称 */
.in-all{
    display: flex;
    align-items:flex-end;
    position: absolute;
    top:96px;
    left:10px;
    z-index: 10;
}
/* 头像 */
.in-all-headimg{
    width:66px;
    height:66px;
    border-radius:33px;
    overflow:hidden;
}
.in-all-headimg>img{
    width:100%;
}
/* 名称 */
.in-all-name{
    font-size:16px;
    padding-left:12px;
    padding-bottom: 8px;
}

.down-all{
    padding-top:50px;
    color:#757575;
    font-size:14px;
    line-height: 1.4;
}

/* 超出隐藏 */
.text-ellipsis{
    text-overflow:ellipsis;
    display:-webkit-box; 
    -webkit-box-orient:vertical;
    -webkit-line-clamp:2;
    overflow: hidden;
}

</style>
