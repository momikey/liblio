import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

/*
 * Store modules
 */
import authentication from './authentication';
import profile from './profile';
import users from './users';

import MockData from './mockdata';

Vue.use(Vuex);

const vuexStorage = new VuexPersistence({
    storage: window.localStorage
})

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
    modules: {
        authentication,
        profile,
        users
    },

    // Add mock data if we're in testing (this will go away eventually)
    state: {
        error: {
            type: null,
            message: ''
        },
        debug,
        ...MockData
    },

    getters: {
        debugMode: state => state.debug
    },

    mutations: {
        setError (state, error) {
            state.error = { ...error };
        },

        clearError (state) {
            state.error = {
                type: null,
                message: ''
            };
        }
    },

    plugins: [vuexStorage.plugin],
    
    strict: debug
});

export default store;