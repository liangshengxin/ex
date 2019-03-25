<template>
  <div id="app">
    <!-- <div id="nav">
       <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link> 
    </div> -->
 
<!-- <transition 
  
  enter-active-class="fadeInLeft" 
  leave-active-class="fadeOutRight"> -->

<!-- <keep-alive include="home">class="animated" style="position:absolute;"  -->
    <keep-alive include="home">
        <router-view ></router-view>
    </keep-alive>

<!-- </keep-alive> -->

<!-- </transition> -->

  </div>
</template>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>

<script>
import md5 from 'js-md5';

export default {
    name:'app',
    beforeMount() {
        // 获取屏幕高度
        this.$store.state.curHeight = document.documentElement.clientHeight
    },
    created(){
        // 设置用户uid
        if (typeof(Storage) !== "undefined") {
            var uid = localStorage.getItem('app:storage:uid')
            if(!uid){
                const date = new Date()
                const randomKey = Math.floor(Math.random()*1000000000); //随机数
                uid = md5(String(date.getTime())+randomKey)
                localStorage.setItem("app:storage:uid",uid) //设个uid
            }
            this.$store.state.uid = uid
        }
    }
}
</script>