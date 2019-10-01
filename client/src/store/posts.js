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
            state.currentThread.splice(0, state.currentThread.length, ...tree);
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
            console.log(post, token);
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
                    console.log(post, token);
                    console.log(err.errors);

                    Snackbar.open({
                        message: `Unable to post: ${err.message}`,
                        type: 'is-danger'
                    })
                })
        },
    }
}