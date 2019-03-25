<template>
<!-- 单图详细页 -->
<div class="c-read">
    <!-- 标题 -->
    <h3 class="up-title">{{infos.title}}</h3>

    <!-- 头像 名称 时间 -->
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
            <div>{{infos.showtime}}</div>
        </div>
    </div>


    <!-- 内容 -->
    <div class="in-centent read-single-max-img">
        <span v-html="infos.content"></span>
    </div>

</div>
</template>

<script>
const content=`
    <p>澎湃新闻 2019-03-01 13:14:47</p><p><img src="http://p3.pstatp.com/large/pgc-image/RJRMpRSHtgp9Qd" alt="外媒：金正恩3月2日中午将乘专列离开越南"/></p><p>2月28日，在越南首都河内，美国总统特朗普（左二）与朝鲜最高领导人金正恩（右二）举行会谈。 新华社 图</p><p>朝鲜最高领导人金正恩将乘专列于当地时间3月2日中午离开越南河内并于当天下午离境。</p><p>据《联合早报》3月1日报道，越南外交部消息人士透露，朝鲜最高领导人金正恩将在当地时间周六（3月2日）中午离开河内，并于当天下午从中越边境越南一侧的同登火车站乘坐专列离境。</p><p>美国总统特朗普与金正恩2月28日在河内的索菲特传奇大都会酒店会晤，但由于双方谈判出现分歧，会谈提前结束。原定会后举行的联合宣言签署仪式临时取消，原定两人共同的工作午餐也被临时取消。</p><p>28日下午，特朗普新闻发布会提前召开，3月1日凌晨0时15分左右，朝鲜外务省突然就第二次“金特会”相关情况在河内举行记者会。</p><p>另据CNN报道，在记者会上，特朗普表示，他和朝鲜最高领导人金正恩暂时没有第三次会谈的计划。</p><p><br/></p>`;
export default {
    name:'readSingle',
    props:{
        infos:Object
    }
}
</script>


<style scoped>
.c-read{
    margin:0 15px;
    padding: 15px 0;
    text-align: left;
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
    font-size:16px;
    padding-left:8px;
}
/* 时间*/
.up-all-right{
    font-size:14px;
    color:#888;
}

/* 标题 */
.up-title{
    font-size:24px;
    line-height: 32px;
}

/* 内容 */
.in-centent{
    font-size: 18px;
    line-height: 1.8;
    width: 100%;
    overflow: hidden;
}
</style>

<style>
.read-single-max-img img{
    width: 100%;
}
.read-single-max-img p{
    padding:8px 0;
}
</style>
