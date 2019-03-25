<template>

  <div class="home">
    <!-- <img alt="Vue logo" v-bind:style="styleObject" src="../assets/logo.png" /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->

<!-- 顶部区域 -->
    <div class="home-top">
        <!-- 轮播图 -->
        <HomeTopSlide></HomeTopSlide>

        <!-- 菜单 -->
        <MeunButton></MeunButton>
    </div>
    
<!-- 底部区域 -->
    <!-- 内容 -->
    <div v-if="$store.state.homeInfoScroll.showBool=='loading' && this.loadingTime.load">
        <span style="color:#999;font-size:14px;">加载中...</span>
    </div>

    <HomeInfoScroll></HomeInfoScroll>
    <!-- <Test></Test> -->
  </div>
</template>

<script>
// @ is an alias to /src
// const HomeTopSlide = () => import('@/components/home/TopSlide.vue')
const MeunButton = () => import('@/components/home/MeunButton.vue')
const HomeInfoScroll = () => import('@/components/home/InfoScroll.vue')

import HomeTopSlide from "@/components/home/TopSlide.vue";
// import MeunButton from "@/components/home/MeunButton.vue";
// import HomeWorld from "@/components/HelloWorld.vue";
// import HomeInfoScroll from "@/components/home/InfoScroll.vue";
// import Test from "@/components/home/Test.vue";

export default {
    name: "home",
    components: {
        HomeTopSlide,
        MeunButton,
        HomeInfoScroll,
        // Test
    },
    data() {
        return {
            loadingTime:{time:1500,load:false}, //延迟显示正在加载 time毫秒 load为true时显示
        }
    },
    created(){
        setTimeout(() => {
            this.loadingTime.load=true
        }, this.loadingTime.time);
    },
    mounted() {
        // 绑定窗口滚动事件
        window.addEventListener('scroll', this.handleScroll)
    },
    methods: {
        handleScroll(){
            
            this.$store.state.curHeight = document.documentElement.clientHeight
        }
    },
    
};
</script>

