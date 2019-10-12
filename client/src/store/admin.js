/*
 * Amin functions
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    namespaced: true,

    state: {
        posts: [],
        postCount: 0,
    },

    getters: {
        posts: state => state.posts,
        postCount: state => state.postCount,
    },

    mutations: {
        setPosts (state, newPosts) {
            state.posts = newPosts;
        },

        clearPosts (state) {
            state.posts = [];
        },

        setPostCount (state, count) {
            state.postCount = count;
        }
    },

    actions: {
        getPosts ({ state, commit }, options) {
            const queryParams = {
                max: options.max,
                page: options.page,
                origin: options.origin,
                sort: options.sort,
                order: options.order
            };

            axios.get('/api/v1/admin/posts', {
                params: queryParams,
                headers: {
                    'Authorization': `Bearer ${options.token}`
                }
            })
                .then(r => {
                    commit('setPosts', r.data.posts);
                    commit('setPostCount', r.data.total);

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to fetch posts: ${err.message}`,
                        type: 'is-danger'
                    });

                    console.error(err);
                })
        }
    }
}