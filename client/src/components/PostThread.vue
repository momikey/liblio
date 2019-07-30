<template>
    <!--
        Liblio threads are flat, not nested.
        This means no need for Themis-style hackery.
    -->
    <section class="post-thread">
        <creator-post-card v-if="parent"
            :post="parent"
        />

        <comment-card v-for="child in children" :key="JSON.stringify(child)"
            :post="child"
        />
    </section>
</template>

<script>
import CreatorPostCard from "@/components/CreatorPostCard.vue";
import CommentCard from "@/components/CommentCard.vue";

export default {
    data () {
        return {

        }
    },

    props: [
        'parent',
        'children'
    ],

    components: {
        CreatorPostCard,
        CommentCard
    }
}
</script>

<style lang="scss">
    .post-thread {
        margin-bottom: 1rem;
    }
</style>
