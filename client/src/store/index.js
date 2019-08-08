import Vue from 'vue';
import Vuex from 'vuex';

import MockData from './mockdata';

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
    modules: {
        
    },

    // Add mock data if we're in testing (this will go away eventually)
    state: {
        ...MockData
    },
    
    strict: debug
});

export default store;