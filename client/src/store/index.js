import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

import authentication from './authentication'

import MockData from './mockdata';

Vue.use(Vuex);

const vuexStorage = new VuexPersistence({
    storage: window.localStorage
})

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
    modules: {
        authentication
    },

    // Add mock data if we're in testing (this will go away eventually)
    state: {
        error: null,
        debug,
        ...MockData
    },

    getters: {
        debugMode: state => state.debug
    },

    mutations: {

    },

    plugins: [vuexStorage.plugin],
    
    strict: debug
});

export default store;