import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import marketing from './modules/marketing';
import analytics from './modules/analytics';
import cart from './modules/cart';
import product from './modules/product';
//Load vuex
Vue.use(Vuex);

//Create store
export default new Vuex.Store({
    modules: {
        user,
        marketing,
        analytics,
        cart,
        product
    }
});