<template>
    <section class="user-post-list">
        <template v-if="currentUserPosts.length">
            <creator-post-card v-for="post in currentUserPosts" :key="post.id"
                :post="post"
            />
        </template>

        <template v-else>
            <p class="no-posts">{{ labels.noPosts }}</p>
        </template>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

import PostThread from '@/components/PostThread.vue';
import CreatorPostCard from '@/components/CreatorPostCard.vue';

export default {
    data () {
        return {
            // TODO: i18n
            labels: {
                noPosts: "No posts found for this user"
            }
        }
    },

    props: [
        'userid'
    ],

    computed: {
        ...mapGetters(['currentUserPosts'])
    },

    mounted () {
        if (this.userid) {
            this.$store.dispatch('getUserPosts', this.userid);
        }
    },

    components: {
        CreatorPostCard,
        PostThread
    }
}
</script>

<style>
    .user-post-list > .section {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
</style>
