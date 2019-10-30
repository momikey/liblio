<template>
    <section class="user-following-list">
        <div class="card" v-for="user in following" :key="user.id">
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
            'following': 'currentUserFollowing'
        })
    },

    components: {
        FollowListEntry,
        TagList
    }
}
</script>

<style>

</style>