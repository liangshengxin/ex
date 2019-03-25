<template>
<div v-bind:style="{height:$store.state.curHeight-parseInt(30)+'px'}">
    <!-- 设置滚动内容高度^ -->

    <!-- 滚动 -->
    <cube-scroll
        ref="scroll"
        :scrollEvents="['scroll-end']"
        :data="$store.state.homeInfoScroll.datas"
        :options="$store.state.homeInfoScroll.options"
        @disable="true"
        @scroll-end="scrollEnd"
        @pulling-down="onPullingDown"
        @pulling-up="onPullingUp"
        >
        <transition-group :name="transitionName" appear mode="in-out" >
            <div
                v-for="(item,key) in $store.state.homeInfoScroll.datas"
                :key="item.id+key"
            >
                <SingleImg v-if="item.category==1" v-bind:infos="item"></SingleImg>
                <NoImg v-if="item.category==2" v-bind:infos="item"></NoImg>
                <AllImg v-if="item.category==3" v-bind:infos="item"></AllImg>
                <RowImg v-if="item.category==4" v-bind:infos="item"></RowImg>
                <MaxImg v-if="item.category==5" v-bind:infos="item"></MaxImg>
                <TextImg v-if="item.category==6" v-bind:infos="item"></TextImg>
            </div>
        </transition-group>
    </cube-scroll>
</div>
</template>

<script>
const SingleImg = () => import('@/components/info/SingleImg.vue')
const RowImg = () => import('@/components/info/RowImg.vue')
const AllImg = () => import('@/components/info/AllImg.vue')
const NoImg = () => import('@/components/info/NoImg.vue')
const MaxImg = () => import('@/components/info/MaxImg.vue')
const TextImg = () => import('@/components/info/TextImg.vue')


export default {
    name:'homeInfoScroll',
    data(){return{
        domnScrollBool:true, //触发允许滚动只执行一次的条件 
        domnScrollTwo:true,  //触发禁止滚动只执行一次的条件
        transitionName:'slide-fade', //初始动画切换
    }},
    created(){
        // 初始化数据
        this.$store.commit('homeInfoScroll/onPullingStart',this)
    },
    mounted() {
        // 绑定窗口滚动事件
        window.addEventListener('scroll', this.handleScroll)
    },
    activated() {
        // 返回时触发 滑动到记录的位置
        //重新计算 better-scroll
        this.$refs.scroll.refresh() 
        //滚动到指定位置
        this.$refs.scroll.scrollTo(0,this.$store.state.homeInfoScroll.scrollEndY,0) //最后一个0 直接滚动到指定位置无缓冲时间

        // 执行一下滚动事件
        this.handleScroll()
    },
    methods:{
        // 下拉刷新
        onPullingDown(){
            this.transitionName='fade' //下拉刷新效果
            this.$store.commit('homeInfoScroll/onPullingDown',this)
        },
        // 上拉加载
        onPullingUp(){
            this.transitionName='slide-fade' //上拉加载效果
            this.$store.commit('homeInfoScroll/onPullingUp',this)
        },
        // 滚动条停止时位置Y
        scrollEnd(res){
            this.$store.state.homeInfoScroll.scrollEndY = res.y
        },

        // 滚动事件
        handleScroll(){

            // 内容距顶部距离
            var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
            // 顶部区域
            var resTop = document.querySelector('.home-top')
            if(!resTop) return false; //未找到元素退出

            resTop = resTop.getBoundingClientRect()
            // 顶部区内容高度
            var homeTopHeight = resTop.height

            // 顶部 触发距离
            this.$store.state.homeInfoScroll.domnScroll = homeTopHeight-scrollTop-30
            // 下按钮元素范围 <2时触发一次允许滚动事件
            if( this.domnScrollBool && this.$store.state.homeInfoScroll.domnScroll<2 ){
                this.$refs.scroll.enable() // 允许滚动
                // this.domnScrollBool=false
                // this.domnScrollTwo=true
            }
            // 下按钮元素范围 >2时触发一次禁止滚动事件
            if(this.domnScrollTwo && this.$store.state.homeInfoScroll.domnScroll>2){
                this.$refs.scroll.disable() // 禁止滚动
                // this.domnScrollTwo=false
                // this.domnScrollBool=true
            }


            var bodys = document.querySelector('body').getBoundingClientRect()

            // 内容距离顶部高度 + 屏幕高度
            var contHei = Math.abs(bodys.top)+this.$store.state.curHeight
            // 底部 触发距离
            var dec = contHei - bodys.height
            if(Math.abs(dec) < 2 ){
                this.$refs.scroll.enable() // 允许滚动
            }else{
                this.$refs.scroll.disable() // 禁止滚动
            }
            
        }
    },
    components:{
        SingleImg,
        RowImg,
        AllImg,
        NoImg,
        MaxImg,
        TextImg
    },
}
</script>


<style>
/* 调整上下刷新显示文字大小 */
.cube-pulldown-loaded,.cube-pullup-wrapper{
    font-size:16px;
}
</style>

<style scoped>
.info-border{
    border-top:1.2px solid #eee;
}
.info-border:first-child{
    border-top:none;
}


.fade-enter-active {
  transition: opacity .5s;
}
.fade-enter/* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}


.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-enter
/* .slide-fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
