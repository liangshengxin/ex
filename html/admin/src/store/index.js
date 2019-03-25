import Vue from "vue";
import Vuex from "vuex";

import navTabs from "./modules/navTabs"
import navMenu from "./modules/navMenu"

Vue.use(Vuex);

export default new Vuex.Store({
    modules:{
        navTabs,
        navMenu,
    },
    mutations: {},
    actions: {}
});

