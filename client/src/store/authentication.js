/*
 * Authentication store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";
import router from '../router';

export default module = {
    state: {
        accessToken: "",
        user: "",
    },

    getters: {
        user: state => state.user,

        accessToken: state => state.accessToken
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

                    router.push('/web');

                    return r;
                })
                .catch(err => {
                    commit('user', '');
                    commit('accessToken', '');

                    console.log(err);
                    
                    Snackbar.open({
                        message: `${err.response.data.message}`,
                        type: 'is-danger'
                    });
                })
        },

        /**
         * Log out of the Liblio server
         *
         * @param { state, commit }
         */
        logout ({ state, commit }) {
            axios.post('/api/v1/auth/logout', null, {
                headers: {
                    'Authorization': `Bearer ${state.accessToken}`
                }
            })
                .then(r => {
                    commit('user', '');
                    commit('accessToken', '');
                    commit('clearProfile');

                    return r;
                })
                .catch(err => {
                    commit('user', '');
                    commit('accessToken', '');
                    commit('clearProfile');
                    
                    Snackbar.open({
                        message: "Could not log out",
                        type: 'is-warning'
                    })

                    console.log(err.response.data);
                })
        },

        /**
         * Create a new account on this server.
         *
         * @param { state, commit }
         * @param { account, profile } The account and profile objects
         * (see server docs for format)
         */
        createAccount({ state, commit }, { account, profile }) {
            axios.post('/api/v1/auth/create-account', {...account})
                .then(r => {
                    // After creating the account, we create the profile
                    axios.post('/api/v1/settings/edit-profile', {...profile}, {
                        headers: {
                            'Authorization': `Bearer ${r.data.temp_token}`
                        }
                    })
                        .then(r => {
                            return r;
                        })
                        .catch(err => {
                            Snackbar.open({
                                message: `Could not create profile: ${err.response.data.message}`,
                                type: 'is-danger'
                            })
                        })

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Could not create account: ${err.response.data.message}`,
                        type: 'is-danger'
                    })
                })
        },

        /**
         * Refresh the user's aPI access token
         *
         * @param { commit }
         * @param token The new token
         */
        refreshToken ({ commit }, token) {
            commit('accessToken', token);
        }
    }
}