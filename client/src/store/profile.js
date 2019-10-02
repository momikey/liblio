/*
 * Profile store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    state: {
        profile: {
            name: '',
            bio: '',
            role: null,
            tags: []
        },
        info: {
            likes: new Set(),
            shares: new Set(),
            followers: new Set(),
            following: new Set()
        }
    },

    getters: {
        myProfile: state => state.profile,

        myLikes: state => state.info.likes,
        myShares: state => state.info.shares,
        myFollowers: state => state.info.followers,
        myFollowed: state => state.info.following,

        isPostLiked: state => id => state.info.likes.has(id),
        isPostShared: state => id => state.info.shares.has(id),
    },

    mutations: {
        profile (state, newProfile) {
            state.profile = { ...newProfile };
        },

        myInfo (state, info) {
            // Object.assign(state.info, info);
            console.log(info, state.info);

            // JSON can't encode sets, so the back end uses arrays instead.
            const addToSet = (set, vals) => vals.forEach(e => set.add(e));

            addToSet(state.info.likes, info.likes);
            addToSet(state.info.shares, info.shares);
            addToSet(state.info.followers, info.followers);
            addToSet(state.info.following, info.following);

            console.log(state.info.likes);
        },

        clearProfile (state) {
            state.profile = {
                name: '',
                bio: '',
                role: null,
                tags: [],
            }
        },

        clearInfo (state) {
            // state.info = {
            //     likes: [],
            //     shares: [],
            //     followers: [],
            //     following: []    
            // }
            state.info.likes.clear();
            state.info.shares.clear();
            state.info.followers.clear();
            state.info.following.clear();
        },

        addLike (state, id) {
            state.likes
        }
    },

    actions: {
        getProfile ({ state, commit, rootGetters }) {
            axios.get('/api/v1/settings/my-profile', {
                headers: {
                    'Authorization': `Bearer ${rootGetters.accessToken}`
                }
            })
                .then(r => {
                    commit('profile', r.data.profile);
                    
                    if (r.data.access_token) {
                        commit('accessToken', r.data.access_token);
                    }

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: "Could not retrieve profile",
                        type: 'is-warning'
                    });

                    console.log(err.response.data);
                })
        },

        getMyInfo ({ commit, rootGetters }) {
            axios.get('/api/v1/settings/me', {
                headers: {
                    'Authorization': `Bearer ${rootGetters.accessToken}`
                }
            })
                .then(r => {
                    commit('myInfo', r.data);

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: "Could not retrieve user data",
                        type: 'is-warning'
                    });

                    console.log(err);
                })
        }

    }
}