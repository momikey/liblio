/*
 * Tags store module
 */

import axios from 'axios';

import { SnackbarProgrammatic as Snackbar } from "buefy";
import router from '../router';

export default module = {
    state: {
        tags: []
    },

    getters: {
        tags: state => state.tags,
        tag: state => (tag) => {
            return state.tags.find(t => t.name == tag);
        }
    },

    mutations: {
        allTags (state, tags) {
            state.tags.splice(0, state.tags.length, ...tags);
        }
    },

    actions: {
        getTagList ({ commit, state }) {
            axios.get('/api/v1/tag')
                .then(r => {
                    commit('allTags', r.data);
                    
                    return r;
                })
                .catch(err => {
                    commit('allTags', []);

                    console.log(err);

                    Snackbar.open({
                        message: err.response.data.message,
                        type: 'is-warning'
                    })
                })
        }
    }
}