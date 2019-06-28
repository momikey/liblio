<template>
    <div class="directory columns">
        <div class="column is-two-thirds" id="directory-column">
            <user-directory-entry v-for="user in visibleUsers" :key="user.id"
                :user="user"
            />
        </div>

        <div class="column is-one-third">
        </div>
    </div>
</template>

<script>

import UserDirectoryEntry from "@/components/UserDirectoryEntry.vue";

import { getAllUsers } from "@/modules/users";

export default {
    data () {
        return {
        }
    },

    computed: {
        users () {
            return getAllUsers(null);
        },

        visibleUsers () {
            return this.users.filter(u => !u.private);
        }
    },

    methods: {
        getAllUsers
    },

    components: {
        UserDirectoryEntry
    }
}
</script>

<style lang="scss">
    #directory-column .card {
        margin: 12px auto;
    }
</style>
