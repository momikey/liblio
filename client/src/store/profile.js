/*
 * Profile store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    state: {
        profile: {
            name: '',
            origin: '',
            bio: '',
            tags: [],
            avatar: '',
            settings: {}
        },
        info: {
            likes: [],
            shares: [],
            followers: [],
            following: []
        },
        notifications: [],
    },

    getters: {
        myProfile: state => state.profile,

        myLikes: state => state.info.likes,
        myShares: state => state.info.shares,
        myFollowers: state => state.info.followers,
        myFollowed: state => state.info.following,

        myNotifications: state => state.notifications,

        isPostLiked: state => id => state.info.likes.indexOf(id) > -1,
        isPostShared: state => id => state.info.shares.indexOf(id) > -1,
    },

    mutations: {
        profile (state, newProfile) {
            state.profile = { ...newProfile };
        },

        myInfo (state, info) {
            Object.assign(state.info, info);
        },

        clearProfile (state) {
            state.profile = {
                name: '',
                origin: '',
                bio: '',
                role: null,
                tags: [],
                avatar: '',
                settings: {}
            }
        },

        clearInfo (state) {
            state.info.likes = [];
            state.info.shares = [];
            state.info.followers = [];
            state.info.following = [];
        },

        updateLikes (state, likes) {
            state.info.likes = likes;
        },

        updateShares (state, shares) {
            state.info.shares = shares;
        },

        updateAvatarUri (state, avatarUri) {
            state.profile.avatar = avatarUri;
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
        },

        updateProfile ({ state, commit, rootGetters }, { newProfile, avatarFile }) {
            axios.post('/api/v1/settings/edit-profile', newProfile, {
                headers: {
                    'Authorization': `Bearer ${rootGetters.accessToken}`
                }
            })
                .then(r => {
                    commit('profile', r.data.profile);

                    if (avatarFile) {
                        const body = new FormData();
                        body.append('avatar', avatarFile);

                        axios.post('/api/v1/settings/edit-avatar', body, {
                            headers: {
                                'Authorization': `Bearer ${rootGetters.accessToken}`
                            }
                        })
                            .then(ar => {
                                commit('updateAvatarUri', ar.headers['location']);

                                Snackbar.open({
                                    message: "Profile updated successfully"
                                })

                                return ar;
                            })
                            .catch(aerr => {
                                Snackbar.open({
                                    message: `Could not update avatar: ${aerr}`,
                                    type: 'is-warning'
                                });
            
                                console.log(aerr);
                            })
                    }

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Could not update profile: ${err}`,
                        type: 'is-warning'
                    });

                    console.log(err);
                })
        }

    }
}