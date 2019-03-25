<template>
<!-- 多图列详细页 -->
<div class="c-read">
    <!-- 标题 -->
    <h3 class="up-title">{{infos.title}}</h3>

    <!-- 头像 名称 时间 -->
    <div class="up-all">
        <!-- 头像名称 -->
        <div class="up-all-left">
            <!-- 头像 -->
            <div class="up-all-left-img">
                <img :src="infos.headimg" />
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
    <div class="in-centent read-row-max-img">
        <span v-html="infos.content"></span>
    </div>

</div>
</template>

<script>
const content=`
    <p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">【环球网综合报道】2020年台湾地区领导人选举越来越近，台北市长柯文哲被视为的热门人选。今天(28日)，柯文哲与台湾地区领导人蔡英文一同出席“2·28”事件纪念仪式，进场时再被问及参选2020的问题，柯没有回应，但尴尬的一幕发生了。</p><p class="imgs_c" style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><img title="1551399572208989.png" alt="image.png" src="http://mpic.haiwainet.cn/thumb/d/uploadfile/20190301/1551399572208989,w_480.png"/></p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">蔡英文（左）柯文哲（右）（来源：台湾“东森新闻云”）</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">经常被曝“全程无互动”的柯文哲与蔡英文因出席“2·28”事件纪念仪式同框，引得岛内媒体关注。据台湾“中时电子报”28日报道，柯文哲在与蔡英文一起入场时被守候在一旁的记者询问，要不要参选2020。</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">报道称，对于记者的提问，走在蔡英文斜后方的柯文哲只是微笑没有回答。而走在前面的蔡英文却突然回头，面带笑意的对柯文哲说，“怎么都是你的问题？”</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">报道形容道，此时“柯文哲笑的更尴尬。”回头看了一眼后面的记者，“不知道是不是上午骑自由车(山地自行车)太累，一不小心脚软了一下，差点跌倒。”</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">对此，台湾网友嘲讽道，记者真有胆量，很不给某人面子喔↓</p><p class="imgs_c" style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><img title="1551399582614462.png" alt="image.png" src="http://mpic.haiwainet.cn/thumb/d/uploadfile/20190301/1551399582614462,w_480.png"/></p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">还有网友认为，蔡英文笑里藏刀;话听起来很酸↓</p><p class="imgs_c" style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><img title="1551399597393022.png" alt="image.png" src="http://mpic.haiwainet.cn/thumb/d/uploadfile/20190301/1551399597393022,w_480.png"/></p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">也有网友回答蔡英文的问话表示，因为蔡英文已经无关重要了↓</p><p class="imgs_c" style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><img title="1551399603281213.png" alt="image.png" src="http://mpic.haiwainet.cn/thumb/d/uploadfile/20190301/1551399603281213,w_480.png"/></p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">关于参选2020，蔡英文日前已通过CNN对外宣布将寻求连任，但柯文哲却始终没有明确回应。</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">此前，“台湾政治大学研究中心”公布民调显示，在2020年的台湾地区领导人选举中，台湾民众对于柯文哲的支持率为38.7%，对于蔡英文的支持率则仅有15.3%。</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">台湾“美丽岛电子报”的民调也显示，若蔡英文、韩国瑜、柯文哲3人竞选台湾地区领导人，韩国瑜支持率为36.6%，柯文哲为28.2%，蔡英文以18.0%的支持率垫底。</p><p style="overflow-wrap: break-word; text-align: justify; margin: 0px 0px 20px; color: rgb(80, 80, 80); line-height: 1.647; padding: 0px; font-family: helvetica; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">对此，柯文哲在22日受访时曾说，“要不要说民调是我的压
    `;
export default {
    name:'readRow',
    data(){
        return{
            infos:{
                headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a4.png',
                name:'北青网',
                showtime:'1小时前',
                title:'华为折叠屏手机要看韩国人脸色？OLED面板产能今年有望华丽转身',
                content:content,
            }
        }
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
.read-row-max-img img{
    width: 100%;
}
.read-row-max-img p{
    padding:8px 0;
}
</style>
