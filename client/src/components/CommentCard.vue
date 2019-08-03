<template>
    <section class="card comment-card">
        <!--
            No title for comments, but we still put the author
            and a timestamp (which we'll make later)
        -->
        <header class="card-header">
            <p class="card-header-title">
                {{ post.title || "" }}
            </p>

            <p class="card-header-title is-size-7 has-text-right liblio-post-author">
                {{ by(post.author) }}
            </p>
        </header>

        <!-- Main comment content -->
        <div class="card-content">
            <div class="content">
                {{ post.content }}
            </div>
        </div>

        <!-- Comment actions -->
        <posting-actions-footer />
    </section>    
</template>

<script>
import PostingActionsFooter from '@/components/PostingActionsFooter.vue';

export default {
    data () {
        return {

        }
    },

    props: [
        'post'
    ],

    methods: {
        by (author) {
            return `by ${author}`;
        }
    },

    components: {
        PostingActionsFooter
    }
}
</script>

<style lang="scss">

</style>
