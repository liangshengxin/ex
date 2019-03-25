<template>
<div v-bind:style="{height:$store.state.curHeight-parseInt(30)+'px'}">
    
    
    
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
                <RowImg v-if="item.category==2" v-bind:infos="item"></RowImg>
                <AllImg v-if="item.category==3" v-bind:infos="item"></AllImg>
                <NoImg v-if="item.category==4" v-bind:infos="item"></NoImg>
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
    data(){return{
        domnScrollBool:true, //触发允许滚动只执行一次的条件 
        domnScrollTwo:true,  //触发禁止滚动只执行一次的条件
        transitionName:'slide-fade', //初始动画切换
    }},
    created(){
        this.$store.commit('homeInfoScroll/onPullingStart',this)
    },
    methods:{
        onPullingDown(){
            this.transitionName='fade' //下拉刷新效果
            this.$store.commit('homeInfoScroll/onPullingDown',this)
        },
        onPullingUp(){
            this.$store.commit('homeInfoScroll/onPullingUp',this)
            this.transitionName='slide-fade' //上拉加载效果

        },
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

            // 触发距离
            this.$store.state.homeInfoScroll.domnScroll = homeTopHeight-scrollTop-30

            // 下按钮元素范围 <2时触发一次允许滚动事件
            if( this.domnScrollBool && this.$store.state.homeInfoScroll.domnScroll<2 ){
                this.$refs.scroll.enable() // 允许滚动
                this.domnScrollBool=false
                this.domnScrollTwo=true
            }

            // 下按钮元素范围 >2时触发一次禁止滚动事件
            if(this.domnScrollTwo && this.$store.state.homeInfoScroll.domnScroll>2){
                this.$refs.scroll.disable() // 禁止滚动
                this.domnScrollTwo=false
                this.domnScrollBool=true
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
    activated() {
        //重新计算 better-scroll
        this.$refs.scroll.refresh() 
        //滚动到指定位置
        this.$refs.scroll.scrollTo(0,this.$store.state.homeInfoScroll.scrollEndY,450)            
    },
    mounted() {
        // 绑定滚动事件
        window.addEventListener('scroll', this.handleScroll)
    },

}
</script>


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
