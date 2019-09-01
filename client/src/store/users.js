/*
 * Users store module.
 */

import axios from "axios";
import { SnackbarProgrammatic as Snackbar } from "buefy";

export default module = {
    state: {
        users: []
    },

    getters: {
        allUsers: state => state.users,
        visibleUsers: state => state.users.filter(u => !u.private)
    },

    mutations: {
        saveUsers (state, u) {
            state.users.splice(0, state.users.length, ...u);
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
        }
    }
}

export function getAllUsers() {
    // Later: API call to the server, fetching all known users;
    // will likely need an API token of some sort.
    return [
        {
            id: 1,
            name: "Test User",
            address: "@test@example.com",
            private: false,
            tags: [
                { key: 'tester', value: 'Tester' },
                { key: 'author', value: 'Author' },
                { key: 'admin', value: 'Administrator' }
            ]
        },
        {
            id: 42,
            name: "Another User",
            address: "@other@example.invalid",
            private: false,
            tags: [
                { key: 'tester', value: 'Tester' },
                { key: 'artist', value: 'Artist' }
            ]
        },
        {
            id: 83,
            name: "Secret Agent",
            address: "@secret@fbi.invalid",
            private: true,
            tags: [
                { key: 'tester', value: 'Tester' }
            ]
        }
    ]
}