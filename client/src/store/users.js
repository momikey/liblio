/*
 * Users store module.
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    state: {
        users: [],
        currentUser: {},
        currentUserPosts: [],
    },

    getters: {
        allUsers: state => state.users,
        visibleUsers: state => state.users.filter(u => !u.private),
        currentUserPosts: state => state.currentUserPosts,
        currentUser: state => state.currentUser,
    },

    mutations: {
        saveUsers (state, users) {
            // state.users.splice(0, state.users.length, ...u);
            state.users = users;
        },

        saveUserPosts (state, posts) {
            // state.currentUserPosts.splice(0, state.currentUserPosts.length, ...posts);
            state.currentUserPosts = posts;
        },

        saveUser (state, user) {
            state.currentUser = user;
        }
    },

    actions: {
        getUserDirectory ({ commit, state }) {
            axios.get('/api/v1/user/public')
                .then(r => {
                    commit('saveUsers', r.data);

                    return r;
                })
                .catch(err => {
                    commit('saveUsers', []);

                    console.log(err);

                    Snackbar.open({
                        message: err.response.data.message,
                        type: 'is-warning'
                    })
                })
        },

        getUserPosts ({ commit, state }, id) {
            axios.get(`/api/v1/user/posts-by-id/${id}`)
                .then(r => {
                    commit('saveUserPosts', r.data);

                    return r;
                })
                .catch(err => {
                    commit('saveUserPosts', []);

                    console.log(err)

                    Snackbar.open({
                        message: "Couldn't fetch posts for this user: ${err.response.data.message}",
                        type: 'is-warning'
                    })
                })
        },

        getUser ({ commit, state }, id) {
            axios.get(`/api/v1/user/by-id/${id}`)
                .then(r => {
                    commit('saveUser', r.data);

                    return r;
                })
                .catch(err => {
                    commit('saveUser', {});

                    console.log(err)

                    Snackbar.open({
                        message: "Couldn't fetch user profile: ${err.response.data.message}",
                        type: 'is-warning'
                    })
                })
        }
    }
}
