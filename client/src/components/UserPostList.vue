<template>
    <section class="user-post-list">
        <creator-post-card v-for="post in currentUserPosts" :key="post.id"
            :post="post"
        />
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

import PostThread from '@/components/PostThread.vue';
import CreatorPostCard from '@/components/CreatorPostCard.vue';

export default {
    data () {
        return {

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

<style lang="scss">

</style>
