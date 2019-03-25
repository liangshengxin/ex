import Vue from "vue";
import Router from "vue-router";


import About from "./views/About.vue"
import HelloWorld from "./components/HelloWorld.vue"
import Content from "./views/Content.vue"
import DbSync from "./views/DbSync.vue"


Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
        path: "/",
        name: "home",
        component: DbSync,
    },
    {
        path:'/db-sync',
        name:'db-sync',
        component:DbSync
    }
    
  ]
});
