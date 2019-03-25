import Vue from "vue";
import Vuex from "vuex";

import homeInfoScroll from "./modules/homeInfoScroll";
import read from "./modules/read";
import homeMenuButtom from "./modules/homeMenuButton";

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        curHeight:0, //屏幕高度
        uid:null, //生成的用户uid
        host:'http://api.lsxin.net',//'http://192.168.44.139', //服务器地址
    },
    modules:{
        homeInfoScroll,
        read,
        homeMenuButtom,
    },
    mutations: {
       
    },
    actions: {}
});

