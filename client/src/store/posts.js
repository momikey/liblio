/*
 * Posts store module
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

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
        }
    }
}