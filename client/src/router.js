import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/web'
        },
        
        {
            path: '/web',
            name: 'home',
            component: Home,
            children: [
                {
                    path: 'user/:userid',
                    name: 'user-profile',
                    component: () => import(/* webpackChunkName: "home" */ './components/UserPostList.vue'),
                    props: true
                }
            ]
        },
        
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        
        {
            path: '/login',
            name: 'login',
            component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
        },
        
        {
            path: '/directory',
            name: 'directory',
            component: () => import(/* webpackChunkName: "user-directory" */ './views/UserDirectory.vue')
        },
        
        {
            path: '/new-account',
            name: 'new-account',
            component: () => import(/* webpackChunkName: "new-account" */ './views/NewAccount.vue')
        },
        
        {
            path: '/sandbox',
            name: 'sandbox',
            component: () => import(/* webpackChunkName: "sandbox" */ './views/Sandbox.vue')
        }
    ]
})
