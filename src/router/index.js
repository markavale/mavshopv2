import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/views/auth/Login';
import Register from '@/views/auth/Register';
import Logout from '@/components/auth/Logout'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Home,
        meta: {
            requiresAuth: false
        }
    },
    {
        path: '/about',
        name: 'about',
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue'),
        meta: {
            requiresAuth: true
        }

    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: {
            requiresLogged: true
        },

    },
    {
        path: '/sign-up',
        name: 'sign-up',
        component: Register,
        meta: {
            requiresLogged: true
        }
    },
    {
        path: '/logout',
        name: 'logout',
        component: Logout,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/mav/auth/password/reset/confirm/:uid/:token/',
        name: 'password-confirm',
        component: () =>
            import ( /* webpackChunkName: "password-confirm" */ '@/views/auth/PasswordConfirm.vue'),
        meta: {
            requiresLogged: true
        }

    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
            routes
        ]
        // authRoutes,
        // todo_routes
})


export default router