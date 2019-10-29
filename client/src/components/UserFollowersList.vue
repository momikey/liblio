<template>
    <section class="user-followers-list">
        <div class="card" v-for="user in followers" :key="user.id">
            <follow-list-entry
                :user="user"
                class="card-content"
            />
            <tag-list  v-if="user.tags" :tags="user.tags" align="left"/>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';
import FollowListEntry from '@/components/FollowListEntry.vue';
import TagList from '@/components/TagList.vue';

export default {
    data () {
        return {

        }
    },

    props: [
        'userid'
    ],

    computed: {
        ...mapGetters({
            'user': 'currentUser',
            'followers': 'currentUserFollowers'
        })
    },

    mounted () {
        this.$store.dispatch('getUserFollowers', this.userid);
    },

    components: {
        FollowListEntry,
        TagList
    }
}
</script>

<style>

</style>