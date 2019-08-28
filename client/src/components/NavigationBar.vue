<template>
    <b-navbar id="nav">
        <template slot="start">
            <b-navbar-item>
                <router-link to="/">Home</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/directory">Users</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/new-account">New Account</router-link>
            </b-navbar-item>

            <b-navbar-item v-if="isDebugMode">
                <router-link to="/sandbox">Sandbox</router-link>
            </b-navbar-item>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <b-dropdown
                    position="is-bottom-left"
                >
                    <a
                        slot="trigger"
                        role="button"
                    >
                        <b-tooltip :label="labels.notifications" animated :delay="500">
                            <b-icon icon="bell"
                                class="has-badge-rounded"
                                :data-badge="unreadFormatted"
                            />
                        </b-tooltip>
                    </a>

                    <b-dropdown-item
                        custom
                        :focusable="false"
                        paddingless
                    >
                        <notifications-list
                            :notifications="notifications"
                        />
                    </b-dropdown-item>
                </b-dropdown>
            </b-navbar-item>

            <b-navbar-item>
                <b-tooltip :label="labels.logout" animated :delay="500"
                    v-if="user"
                >
                    <a role="button"
                        @click="onLogout"
                    >
                        <b-icon icon="logout" />
                    </a>
                </b-tooltip>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import axios from 'axios'; 

import NotificationsList from '@/components/NotificationsList.vue';

export default {
    data () {
        return {
            notifications: this.$store.state.notifications,

            testingText: "",

            labels: {
                notifications: "Notifications",
                logout: "Log out"
            }
        }
    },

    computed: {
        unreadNotifications () {
            return this.notifications.filter(n => n.unread).length
        },

        unreadFormatted () {
            const unread = this.unreadNotifications;

            if (unread == 0) {
                return false;
            } else if (unread >= 100) {
                return "99+";
            } else {
                return unread;
            }
        },

        user () {
            return this.$store.getters.user || true;
        },

        isDebugMode () {
            return this.$store.getters.debugMode;
        }
    },

    methods: {
        onLogout () {
            this.$store.dispatch('logout')
        }
    },

    components: {
        NotificationsList
    }
}
</script>
