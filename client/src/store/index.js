import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

import MockData from './mockdata';

Vue.use(Vuex);

const vuexStorage = new VuexPersistence({
    storage: window.localStorage
})

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
    modules: {
        
    },

    // Add mock data if we're in testing (this will go away eventually)
    state: {
        debug,
        ...MockData
    },

    getters: {
        debugMode: state => state.debug
    },

    plugins: [vuexStorage.plugin],
    
    strict: debug
});

export default store;