<template>
    <section class="timeline">
        <template v-for="post in timeline">
            <creator-post-card :key="post.id" v-if="!post.parent_id"
                :post="post"
            />

            <comment-card :key="post.id" v-else
                :post="post"
            />
        </template>
    </section>
</template>

<script>
import CreatorPostCard from '@/components/CreatorPostCard.vue';
import CommentCard from '@/components/CommentCard.vue';

import { mapGetters } from 'vuex';

export default {
    data () {
        return {

        }
    },

    computed: {
        ...mapGetters([
            'timeline'
        ])
    },

    mounted () {
        this.$store.dispatch('getPublicPosts', {});
    },

    components: {
        CreatorPostCard,
        CommentCard
    }
}
</script>

<style>
    .timeline .card {
        margin: 1rem auto;
    }
</style>