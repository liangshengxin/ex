<template>
    <div class='home-top-slide'>
        <cube-slide :data="items"></cube-slide>
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
</style>
