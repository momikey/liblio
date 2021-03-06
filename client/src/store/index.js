import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

/*
 * Store modules
 */
import admin from './admin';
import authentication from './authentication';
import posts from './posts';
import profile from './profile';
import tags from './tags';
import users from './users';

import MockData from './mockdata';

Vue.use(Vuex);

const vuexStorage = new VuexPersistence({
    storage: window.localStorage
})

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
    modules: {
        admin,
        authentication,
        posts,
        profile,
        tags,
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
        debugMode: state => state.debug,
        host: state => state.debug ? "localhost:5000" : window.location.host
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