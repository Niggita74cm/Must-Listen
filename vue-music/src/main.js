import Vue from 'vue'
import App from './App.vue'

import router from  '@/router/index.js'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import axios from 'axios'
import VueAxios from 'vue-axios'

import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

Vue.component('vue-slick-carousel', VueSlickCarousel)

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueAxios, axios);
Vue.use(router)

Vue.config.productionTip = false


axios.defaults.withCredentials = true;
axios.defaults.baseURL = '/';  // the FastAPI backend

new Vue({  
  render: h => h(App),
  router,
  axios  
}).$mount('#app')

//new Vue({
  //el: '#app',
  //components: { App },
  //template: '<App/>',
  //axios
 //}).$mount('#app')