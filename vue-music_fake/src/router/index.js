import Vue from 'vue';
import Router from 'vue-router';
import AuthUser from '@/components/AuthUser.vue';


Vue.use(Router);

export default new Router({
 mode: 'history',
 routes: [
    {
        path: '/',
        name: 'AuthUser',
        component: AuthUser
   }
 ],
});