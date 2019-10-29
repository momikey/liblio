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
        currentUserFollowers: [],
        currentUserFollowing: [],
    },

    getters: {
        allUsers: state => state.users,
        visibleUsers: state => state.users.filter(u => !u.private),
        currentUser: state => state.currentUser,
        currentUserPosts: state => state.currentUserPosts,
        currentUserFollowers: state => state.currentUserFollowers,
        currentUserFollowing: state => state.currentUserFollowing,
    },

    mutations: {
        saveUsers (state, users) {
            state.users = users;
        },

        saveUser (state, user) {
            state.currentUser = user;
        },

        saveUserPosts (state, posts) {
            state.currentUserPosts = posts;
        },

        saveUserFollowers (state, followers) {
            state.currentUserFollowers = followers;
        },

        saveUserFollowing (state, following) {
            state.currentUserFollowing = following;
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
        },

        getUserFollowers ({ commit, state }, id) {
            axios.get(`/api/v1/user/followers/${id}`)
                .then(r => {
                    commit('saveUserFollowers', r.data);

                    return r;
                })
                .catch(err => {
                    commit('saveUserFollowers', []);

                    console.log(err)

                    Snackbar.open({
                        message: "Couldn't fetch followers: ${err.response.data.message}",
                        type: 'is-warning'
                    })
                })
        },

        getUserFollowing ({ commit, state }, id) {
            axios.get(`/api/v1/user/following/${id}`)
                .then(r => {
                    commit('saveUserFollowing', r.data);

                    return r;
                })
                .catch(err => {
                    commit('saveUserFollowing', []);

                    console.log(err)

                    Snackbar.open({
                        message: "Couldn't fetch follow list: ${err.response.data.message}",
                        type: 'is-warning'
                    })
                })
        },
    }
}
