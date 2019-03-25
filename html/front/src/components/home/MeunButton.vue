<template>
    <div class="home-meun-button">

        <!-- 一层 换行 -->
        <div class="edit-button" v-for="(data,key) in $store.state.homeMenuButtom.list" :key="key">
            <!-- 二层 按钮 -->
            <router-link class="edut-button-down" :to="'/category/'+item.id" v-for="item in data" :key="item.name">
                <i :class="item.icon" :style="{color:item.color}"></i>
                <p>{{item.name}}</p>
            </router-link>
        </div>
        <div class="menu-down" @click="menuDown">
            <i class="cubeic-pulldown"></i>
        </div>
    </div>
</template>

<script>
export default {
    name:'homeMeunButton',
    methods: {
        // 点击下按钮将滚动条移动到 指定位置
        menuDown(){
            // 顶部区域
            var resTop = document.querySelector('.home-top')
            if(!resTop) return false; //未找到元素退出

            resTop = resTop.getBoundingClientRect()
            // 顶部区内容高度
            var homeTopHeight = resTop.height

            // 大于2时移动到内容区域 
            if(this.$store.state.homeInfoScroll.domnScroll>2){
                window.pageYOffset=homeTopHeight
                document.documentElement.scrollTop=homeTopHeight
                document.body.scrollTop=homeTopHeight
            }else{
                // 否则移动到顶部
                window.pageYOffset=0
                document.documentElement.scrollTop=0
                document.body.scrollTop=0
            }
            
        }
    },
}
</script>


<style scoped>
.edit-button{
    display:flex;
    flex-direction:row;
    justify-content:space-around;
    margin-top:20px;
}

/* 文字大小和距离 */
.edut-button-down>p{
    font-size:14px;
    padding-top: 8px;
}
.iconfont{
    font-size:42px;
}

/* down */
.menu-down{
    /* height:20px; */
    /* background:#666; */
    color:#FE9700;
    font-size:30px;
    padding-top:5px;
}
</style>

