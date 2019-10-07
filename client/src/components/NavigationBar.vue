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
                <router-link to="/explore">Explore</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/new-account">New Account</router-link>
            </b-navbar-item>

            <b-navbar-item v-if="isAdmin">
                <router-link to="/admin">Admin Panel</router-link>
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
                            :notifications="myNotifications"
                        />
                    </b-dropdown-item>
                </b-dropdown>
            </b-navbar-item>

            <b-navbar-item v-if="user">
                <b-tooltip :label="labels.logout" animated :delay="500"
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
import NotificationsList from '@/components/NotificationsList.vue';
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            labels: {
                notifications: "Notifications",
                logout: "Log out"
            }
        }
    },

    computed: {
        ...mapGetters([
            'myNotifications',
            'isAdmin'
        ]),

        unreadNotifications () {
            return this.myNotifications.filter(n => n.unread).length
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
            return this.$store.getters.user || false;
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
