import Vue from 'vue';
import Router from 'vue-router';
import RegistrUserPage from '@/components/RegistrUserPage.vue';
import AuthUser from '@/components/AuthUser.vue';
import MainPage from '@/components/MainPage.vue';

import SettingsFirst from '@/components/SettingsFirst.vue'
import SearchResults from '@/components/SearchResults.vue'
import MusicPage from '@/components/MusicPage.vue'
import AuthUser_2factor from '@/components/AuthUser_2factor.vue'


Vue.use(Router);

export default new Router({
 mode: 'history',
 routes: [
    {
        path: '/',
        name: 'AuthUser',
        component: AuthUser
   },
   {
     path: '/RegistrUserPage',
     name: 'RegistrUserPage',
     component: RegistrUserPage,
   },
   {
    path: '/MainPage',
    name: 'MainPage',
    component: MainPage,
  },
  {
    path: '/SettingsF',
    name: 'SettingsFirst',
    component: SettingsFirst,
  },
  {
    path: '/SearchResults',
    name: 'SearchResults',
    component: SearchResults,
  },
  {
    path: '/music/:id',
    name: 'MusicPage',
    component: MusicPage,
  },
  {
    path: '/2factor',
    name: 'AuthUser_2factor',
    component: AuthUser_2factor,
  },
 ],
});