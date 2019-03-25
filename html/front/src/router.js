import Vue from "vue";
import Router from "vue-router";

import Home from "./views/Home.vue";
// import Read from "./views/Read.vue";
// import Category from "./views/Category.vue";

const Read = () => import('./views/Read.vue')
const Category = () => import('./views/Category.vue')



Vue.use(Router);

export default new Router({
  mode: "hash",//history 看路由mode项
  base: "/",//process.env.BASE_URL,

  // 滚动行为
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
        return savedPosition
    } else {
        return { x: 0, y: 0 }
    }
  },
  
  routes: [
    {
        path: "/",  //首页
        name: "home",
        component: Home
    },
    {
        path:"/read/:id/:category", // id / 类型  指定内容页
        name: "read",
        component:Read
    },
    {
        path:"/category/:id", // id类型  指定类别页
        name: "category",
        component:Category
    },
    // {
    //   path: "/about",
    //   name: "about",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "./views/About.vue")
    // }
  ]
});
