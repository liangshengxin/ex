<template>
    <div class='home-top-slide'>
        <cube-slide 
            ref="slide" 
            :data="items"
            @change="changePage">
            <cube-slide-item v-for="(item, index) in items" :key="index" @click.native="clickHandler(item, index)">
                <a :href="item.url">
                    <img class="slide-img" style="width:100%;" v-lazy="item.image">
                </a>
            </cube-slide-item>
        </cube-slide>
    </div>
</template>

<script>
export default {
    name: "homeTopSlide",
    data() {
        return {
            items: [
                {
                    url:'#',
                    image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/fl01.png',
                },
                {
                    url:'#',
                    image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/fl02.png',
                },
                {
                    url:'#',
                    image:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/fl03.png',
                }
            ]
        }
    },
    methods: {
        changePage(current){
            // console.log('当前轮播图序号为:' + current)
        },
        clickHandler(item, index) {
            this.$createToast({
                time: 600,
                txt: '开发中',
                type:'txt',
            }).show()
            
        }
    },
    // created(){
    //     const toast = this.$createToast({
    //         time: 0,
    //             txt: '加载中'
    //         })
    //     // toast.show()
    //     axios.get('http://192.168.44.137/json')
    //     // .then(response=>(this.items=response.data))
    //   .catch(error => {
    //     console.log(error)
    //   })
    //   .then(function(){
    //       toast.hide()
    //   })
    //   .finally(() => console.log('finally'))
    // }
}
</script>


<style scoped>
.home-top-slide{
    height:177px;
    width:375px;
}
.slide-img{
    width:100%;
}
</style>
