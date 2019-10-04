/*
 * Authentication store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";
import router from '../router';

export default module = {
    state: {
        accessToken: "",
        refreshToken: "",
        user: "",
        apiPoll: null
    },

    getters: {
        user: state => state.user,

        accessToken: state => state.accessToken,

        refreshToken: state => state.refreshToken
    },

    mutations: {
        accessToken (state, token) {
            state.accessToken = token;
        },

        user (state, username) {
            state.user = username;
        },

        setApiPollId (state, id) {
            state.apiPoll = id;
        },

        clearApiPollId (state) {
            state.apiPoll = null;
        },

        setRefreshToken (state, token) {
            state.refreshToken = token;
        },
    },

    actions: {
        /**
         * Log into the Liblio server.
         *
         * @param { state, commit } Vuex store
         * @param credentials An object containing a username and password
         */
        login ({ state, commit, dispatch }, credentials) {
            axios.post('/api/v1/auth/login', credentials)
                .then(r => {
                    commit('user', credentials.username);
                    commit('accessToken', r.data.access_token);
                    commit('setRefreshToken', r.data.refresh_token);

                    // router.push('/');
                    dispatch('initiateRefresh');

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
            window.clearInterval(state.apiPoll);
            commit('clearApiPollId')

            axios.post('/api/v1/auth/logout', null, {
                headers: {
                    'Authorization': `Bearer ${state.accessToken}`
                }
            })
                .then(r => {
                    commit('user', '');
                    commit('accessToken', '');
                    commit('clearProfile');
                    commit('clearInfo');

                    return r;
                })
                .catch(err => {
                    commit('user', '');
                    commit('accessToken', '');
                    commit('clearProfile');
                    commit('clearInfo');
                    
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
         * Start refreshing the API token at 5 minute intervals.
         * Access tokens are good for 15 minutes, so the idea is
         * that this gives us a couple of retries.
         *
         * @param { commit, dispatch }
         */
        initiateRefresh({ commit, dispatch }) {
            commit('setApiPollId', window.setInterval(() => {
                dispatch('refreshToken');
            }, 5 * 60 * 1000));
        },

        /**
         * Refresh the user's aPI access token
         *
         * @param { commit }
         * @param token The new token
         */
        refreshToken ({ state, commit }) {
            axios.post('/api/v1/auth/refresh', {}, {
                headers: {
                    'Authorization': `Bearer ${state.refreshToken}`
                }
            })
                .then(r => {
                    commit('accessToken', r.data.access_token);
                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: "Unable to refresh API token",
                        type: 'is-warning'
                    })
                })
        }
    }
}