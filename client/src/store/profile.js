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
    },

    getters: {
        myProfile: state => state.profile
    },

    mutations: {
        profile (state, newProfile) {
            state.profile = { ...newProfile };
        },

        clearProfile (state) {
            state.profile = {
                name: '',
                bio: '',
                role: null,
                tags: []
            }
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
        }

    }
}