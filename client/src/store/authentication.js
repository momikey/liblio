/*
 * Authentication store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    state: {
        accessToken: "",
        user: "",
    },

    getters: {
        user: state => state.user
    },

    mutations: {
        accessToken (state, token) {
            state.accessToken = token;
        },

        user (state, username) {
            state.user = username;
        }
    },

    actions: {
        /**
         * Log into the Liblio server.
         *
         * @param { state, commit } Vuex store
         * @param credentials An object containing a username and password
         */
        login ({ state, commit }, credentials) {
            axios.post('/api/v1/auth/login', credentials)
                .then(r => {
                    commit('user', credentials.username);
                    commit('accessToken', r.data.access_token);
                    return r;
                })
                .catch(err => {
                    commit('user', '');
                    commit('accessToken', '');
                    
                    Snackbar.open({
                        message: `${err.response.data.message}`,
                        type: 'is-danger'
                    });
                })
        },

        logout ({ state, commit }) {
            axios.post('/api/v1/auth/logout', null, {
                headers: {
                    'Authorization': `Bearer ${state.accessToken}`
                }
            })
                .then(r => {
                    commit('user', '');
                    commit('accessToken', '');
                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: "Could not log out",
                        type: 'is-warning'
                    })

                    console.log(err.response.data);
                })
        }
    }
}