<template>
    <b-navbar id="nav">
        <template slot="start">
            <b-navbar-item>
                <router-link to="/">Home</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/login">Login</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/directory">Users</router-link>
            </b-navbar-item>

            <b-navbar-item>
                <router-link to="/new-account">New Account</router-link>
            </b-navbar-item>
        </template>

        <template slot="end">
            <b-navbar-item>
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
                </b-dropdown>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {
    data () {
        return {
            labels: {
                notifications: "Notifications",
            }
        }
    },

    computed: {
        unreadNotifications () {
            // TODO API call, etc.
            return 0;
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
        }
    }
}
</script>
