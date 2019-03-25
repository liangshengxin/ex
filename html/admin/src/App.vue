<template>
  <div id="app">
        <!-- 菜单 -->
        <Menu></Menu>
        
        <router-view ></router-view>
  </div>
</template>

<script>
import Menu from "@/components/nav/Menu.vue"

export default {
  name: 'app',
  components: {
    Menu
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

*{margin:0;padding:0;}
</style>
