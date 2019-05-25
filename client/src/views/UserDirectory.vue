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

export default {
    data () {
        return {
            users: [
                { id: 1, name: "Test", address: "@test@example.com" },
                { id: 42, name: "Other", address: "@other@example.invalid" },
                { id: 83, name: "Secret", address: "@secret@fbi.invalid", private: true }
            ]
        }
    },

    computed: {
        visibleUsers () {
            return this.users.filter(u => !u.private);
        }
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
