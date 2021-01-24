import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/auth/Login';
import Register from '@/views/auth/Register';
import Logout from '@/components/auth/Logout'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'index',
        component: () =>
            import ( /* webpackChunkName: "index" */ '../views/Index.vue'),
        meta: {
            requiresAuth: false,
            title: 'Index',
            breadCrumb: 'Home'
        }
    },
    {
        path: '/:itemType/:slug',
        name: 'item',
        component: () =>
            import ( /* webpackChunkName: "product" */ '../views/product/Product.vue'),
        meta: {
            requiresAuth: false,
            title: 'Item Details',
            // breadCrumb: 'Item Instance'
        },
        // props: (route) => ({ item: route.query.slug })  

    },
    // {
    //     path: '/product',
    //     name: 'product',
    //     component: () =>
    //         import ( /* webpackChunkName: "product" */ '../views/product/Product.vue'),
    //     meta: {
    //         requiresAuth: false,
    //         title: 'product'
    //     }

    // },
    {
        path: '/shop',
        name: 'shop',
        component: () =>
            import ( /* webpackChunkName: "shop" */ '../views/Shop.vue'),
        meta: {
            requiresAuth: false,
            title: 'shop',
            breadCrumb: 'Item Type'
        }

    },
    {
        path: '/order-summary',
        name: 'order-summary',
        component: () =>
            import ( /* webpackChunkName: "order-summary" */ '../views/OrderSummary.vue'),
        meta: {
            requiresAuth: false,
            title: 'Orders Summary',
            breadCrumb: 'Order Summary'
        }

    },
    {
        path: '/wish-list',
        name: 'wish-list',
        component: () =>
            import ( /* webpackChunkName: "wish-list" */ '../views/accounts/WishList.vue'),
        meta: {
            requiresAuth: true,
            title: 'My Wish List',
            breadCrumb: 'Item Type'
        }
    },
    {
        path: '/about',
        name: 'about',
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue'),
        meta: {
            requiresAuth: true,
            title: 'About Me'
        }

    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: {
            requiresLogged: true,
            title: 'Login'
        },

    },
    {
        path: '/sign-up',
        name: 'sign-up',
        component: Register,
        meta: {
            requiresLogged: true,
            title: 'Sign Up'
        }
    },
    {
        path: '/logout',
        name: 'logout',
        component: Logout,
        meta: {
            requiresAuth: true,
            title: 'Logout'
        }
    },
    {
        path: '/mav/auth/password/reset/confirm/:uid/:token/',
        name: 'password-confirm',
        component: () =>
            import ( /* webpackChunkName: "password-confirm" */ '@/views/auth/PasswordConfirm.vue'),
        meta: {
            requiresLogged: true,
            title: 'Passoword Confirm'
        }

    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
    // authRoutes,
    // todo_routes
})


export default router