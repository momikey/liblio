/*
 * Amin functions
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    namespaced: true,

    state: {
        /*
         * Note that we store the count of all entities (user, post, tags),
         * as a second data attribute, because we may only load a small portion
         * of the entire set of these, but the front end needs to know the total
         * count for pagination purposes.
         */
        posts: [],
        postCount: 0,

        tags: [],
        tagCount: 0,

        users: [],
        userCount: 0,

        media: [],
        mediaCount: 0
    },

    getters: {
        posts: state => state.posts,
        postCount: state => state.postCount,

        tags: state => state.tags,
        tagCount: state => state.tagCount,

        users: state => state.users,
        userCount: state => state.userCount,

        media: state => state.media,
        mediaCount: state => state.mediaCount
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
        },

        setTags (state, newTags) {
            state.tags = newTags;
        },

        clearTags (state) {
            state.tags = [];
        },

        setTagCount (state, count) {
            state.tagCount = count;
        },

        setUsers (state, newUsers) {
            state.users = newUsers;
        },

        clearUsers (state) {
            state.users = [];
        },

        setUserCount (state, count) {
            state.userCount = count;
        },

        setMedia (state, newMedia) {
            state.media = newMedia;
        },

        clearMedia (state) {
            state.media = [];
        },

        setMediaCount (state, count) {
            state.mediaCount = count;
        }
    },

    actions: {
        // TODO: Fix up backend sorting for all of these
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
        },

        getUsers ({ state, commit }, options) {
            const queryParams = {
                max: options.max,
                page: options.page,
                origin: options.origin,
                sort: options.sort,
                order: options.order
            };

            const endpoint = `/api/v1/admin/${options.mode === 'all' ? 'users' : 'accounts'}`;
            axios.get(endpoint, {
                params: queryParams,
                headers: {
                    'Authorization': `Bearer ${options.token}`
                }
            })
                .then(r => {
                    commit('setUsers', r.data.users);
                    commit('setUserCount', r.data.total);

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to fetch users: ${err.message}`,
                        type: 'is-danger'
                    });

                    console.error(err);
                })
        },

        getTags ({ state, commit }, options) {
            const queryParams = {
                max: options.max,
                page: options.page,
                sort: options.sort,
                order: options.order
            };

            axios.get('/api/v1/admin/tags', {
                params: queryParams,
                headers: {
                    'Authorization': `Bearer ${options.token}`
                }
            })
                .then(r => {
                    commit('setTags', r.data.tags);
                    commit('setTagCount', r.data.total);

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to fetch tags: ${err.message}`,
                        type: 'is-danger'
                    });

                    console.error(err);
                })
        },

        getMedia ({ state, commit }, options) {
            const queryParams = {
                max: options.max,
                page: options.page,
                sort: options.sort,
                order: options.order
            };

            axios.get('/api/v1/admin/uploads/media', {
                params: queryParams,
                headers: {
                    'Authorization': `Bearer ${options.token}`
                }
            })
                .then(r => {
                    commit('setMedia', r.data.uploads);
                    commit('setMediaCount', r.data.total);

                    return r;
                })
                .catch(err => {
                    Snackbar.open({
                        message: `Unable to fetch uploaded media: ${err.message}`,
                        type: 'is-danger'
                    });

                    console.error(err);
                })
        }
    }
}