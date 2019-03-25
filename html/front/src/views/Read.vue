<template>
<div class="read">
<transition name="fade" appear mode="in-out" >
    <div v-if="$store.state.read.showBool=='loading' && this.loadingTime.load">
        <!-- <span>加载中</span> -->
        <cube-loading></cube-loading>
    </div>
    <div v-else-if="$store.state.read.showBool=='error'">
        <div style="margin-top:20px;color:#999">加载失败</div>
    </div>
    <div v-else-if="$store.state.read.showBool=='success'">
        <readSingle v-bind:infos="$store.state.read.datas" v-if="$route.params.category==1"></readSingle>
        <readSingle v-bind:infos="$store.state.read.datas" v-if="$route.params.category==2"></readSingle>
        <!-- <readRow></readRow> -->
    </div>
    
</transition>
</div>
</template>

<script>
import readSingle from '@/components/read/Single.vue'; //单图列详细信息
// import readRow from '@/components/read/Row.vue'; //多图列详细信息
/**
const infos = {
    headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a4.png',
    name:'中国社会网',
    showtime:'2小时前',
    title:'华为折叠屏手机要看韩国人脸色？OLED面板产能今年有望华丽转身',
    content:'content',
}
 */


export default {
    name:'read',
    components:{
        readSingle,
        // readRow
    },
    data() {
        return {
            loadingTime:{time:1000,load:false} //延迟显示正在加载 time毫秒 load为true时显示
        }
    },
    created(){
        this.$store.state.read.showBool='loading' //初始化为loading 显示正在加载

        setTimeout(() => {
            this.loadingTime.load=true
        }, this.loadingTime.time);

        var id = this.$route.params.id //id
        this.$store.commit('read/initGet',id)
    },
}
</script>


<style scoped>
.loading{
    text-align:center;
}
.fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
}
</style>

