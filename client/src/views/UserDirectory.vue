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

import { mapGetters } from "vuex";

import UserDirectoryEntry from "@/components/UserDirectoryEntry.vue";

export default {
    data () {
        return {
        }
    },

    computed: {
        ...mapGetters([
            'allUsers',
            'visibleUsers'
        ]),
    },

    methods: {
    },

    components: {
        UserDirectoryEntry
    },

    mounted () {
        this.$store.dispatch('getUserDirectory');
        console.log(this.allUsers);
    }
}
</script>

<style lang="scss">
    #directory-column .card {
        margin: 12px auto;
    }
</style>
