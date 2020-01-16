import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import AdminPanel from './views/admin-panel/AdminPanel.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/web'
        },
        
        {
            path: '/web',
            component: Home,
            children: [
                {
                    path: '',
                    name: 'timeline',
                    component: () => import(/* webpackChunkName: "home" */ './views/Timeline.vue')
                },

                {
                    path: 'user/:userid',
                    name: 'user-profile',
                    component: () => import(/* webpackChunkName: "home" */ './views/UserProfile.vue'),
                    props: true,
                    children: [
                        {
                            path: '',
                            alias: 'posts',
                            name: 'user-posts',
                            component: () => import(/* webpackChunkName: "home" */ './components/UserPostList.vue'),
                        },
                        {
                            path: 'followers',
                            name: 'user-followers',
                            component: () => import(/* webpackChunkName: "home" */ './components/UserFollowersList.vue'),
                        },
                        {
                            path: 'following',
                            name: 'user-following',
                            component: () => import(/* webpackChunkName: "home" */ './components/UserFollowingList.vue'),
                        }
                    ]
                },

                {
                    path: 'tag/:tagname',
                    name: 'tag-display',
                    component: () => import(/* webpackChunkName: "home" */ './views/TagDisplay.vue'),
                    props: true
                },

                {
                    path: 'post/:postid',
                    name: 'post-display',
                    component: () => import(/* webpackChunkName: "home" */ './views/ThreadDisplay.vue'),
                    props: true
                },

                {
                    path: 'new-post',
                    name: 'new-post',
                    component: () => import(/* webpackChunkName: "home" */ './views/NewPost.vue'),
                },

                {
                    path: 'new-announcement',
                    name: 'new-announcement',
                    component: () => import(/* webpackChunkName: "home" */ './views/NewWorkPost.vue'),
                },

                {
                    path: 'profile',
                    name: 'my-profile',
                    component: () => import(/* webpackChunkName: "home" */ './views/ProfileEditor.vue'),
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
            path: '/explore',
            name: 'explore',
            component: () => import(/* webpackChunkName: "explore-tags" */ './views/ExploreTags.vue')
        },
        
        {
            path: '/new-account',
            name: 'new-account',
            component: () => import(/* webpackChunkName: "new-account" */ './views/NewAccount.vue')
        },
        
        {
            path: '/admin',
            name: 'admin',
            component: AdminPanel,
            children: [
                {
                    path: 'users/:mode',
                    name: 'admin-users',
                    component: () => import(/* webpackChunkName: "admin" */ './views/admin-panel/Users.vue'),
                    props: true
                },
                {
                    path: 'posts/:mode',
                    name: 'admin-posts',
                    component: () => import(/* webpackChunkName: "admin" */ './views/admin-panel/Posts.vue'),
                    props: true
                },
                {
                    path: 'tags',
                    name: 'admin-tags',
                    component: () => import(/* webpackChunkName: "admin" */ './views/admin-panel/Tags.vue'),
                },
                {
                    path: 'uploads',
                    name: 'admin-uploads',
                    component: () => import(/* webpackChunkName: "admin" */ './views/admin-panel/Uploads.vue'),
                },
                {
                    path: 'settings',
                    name: 'admin-settings',
                    component: () => import(/* webpackChunkName: "admin" */ './views/admin-panel/Settings.vue'),
                },
            ]
        },
    ]
})
