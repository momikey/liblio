import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('./views/About.vue')
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    },

    {
      path: '/directory',
      name: 'directory',
      component: () => import('./views/UserDirectory.vue')
    },

    {
      path: '/new-account',
      name: 'new-account',
      component: () => import('./views/NewAccount.vue')
    },

    {
      path: '/sandbox',
      name: 'sandbox',
      component: () => import('./views/Sandbox.vue')
    }
  ]
})
