import Vue from "vue";
import './plugins/axios'

import App from "./App.vue";
import store from "./store/index";

import 'amfe-flexible';
// import animate from 'animate.css'; //css动画
import vueLazyLoad from "vue-lazyload";
import './assets/iconfont/iconfont.css'
import router from "./router";

Vue.use(vueLazyLoad,{
    loading:require('./assets/loading-1.png'), //图片未加载出来时默认图
    error:require('./assets/loading-1.png'), //图片出错显示默认图
    attempt:3, //尝试次数
});
// import cube from "cube-ui";
// Vue.use(cube)
import {
  Style,
  Button,
  ImagePreview,
  Slide,
  Toast,
  scrollNavBar,
  Scroll,

} from "cube-ui";
Vue.use(Button);
Vue.use(ImagePreview);
Vue.use(Slide);
Vue.use(Toast);
Vue.use(scrollNavBar);
Vue.use(Scroll);


Vue.config.productionTip = true;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
