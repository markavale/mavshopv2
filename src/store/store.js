import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import marketing from './modules/marketing';
//Load vuex
Vue.use(Vuex);

//Create store
export default new Vuex.Store({
    modules: {
        user,
        marketing
    }
});