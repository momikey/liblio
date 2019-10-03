/*
 * Posts store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";
import router from "../router";

export default module = {
    state: {
        currentThread: []
    },

    getters: {
        thread: state => state.currentThread,
        threadParent: state => state.currentThread.length ? state.currentThread[0] : null,
        threadChildren: state => state.currentThread.length ? state.currentThread.slice(1) : []
    },

    mutations: {
        thread (state, tree) {
            // state.currentThread.splice(0, state.currentThread.length, ...tree);
            state.currentThread = tree;
        },
    },

    actions: {
        getThread ({ commit }, parentId) {
            axios.get(`/api/v1/post/tree/${parentId}`)
                .then(r => {
                    commit('thread', r.data);
                    return r;
                })
                .catch(err => {
                    commit('thread', [])

                    Snackbar.open({
                        message: "Couldn't retrieve thread",
                        type: 'is-warning'
                    })
                })
        },

        newPost ({ commit }, { post, token }) {
            let body = {
                subject: post.subject,
                source: post.body,
                /* TODO: Tag support */
                /* tags: post.tags */
            };

            if (post.parent) {
                body.parent = post.parent;
            }

            axios.post('/api/v1/post/new', body, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
                .then(r => {
                    router.push("/web");
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to post: ${err.message}`,
                        type: 'is-danger'
                    })
                })
        },

        likePost ({ commit }, { postId, token }) {
            axios.post(`/api/v1/post/like/${postId}`, {
                // Likes don't really need a request body, do they?
            }, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
                .then(r => {
                    commit('updateLikes', r.data.likes, { root: true });
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to like post: ${err.message}`,
                        type: 'is-warning'
                    })

                    console.log(err);
                })
        },

        sharePost ({ commit }, { postId, token }) {
            axios.post(`/api/v1/post/share/${postId}`, {}, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
                .then(r => {
                    commit('updateShares', r.data.sharing, { root: true });
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to share post: ${err.message}`,
                        type: 'is-warning'
                    })

                    console.log(err);
                })
        }
    }
}