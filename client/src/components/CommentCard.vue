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
        <posting-actions-footer
            @action-reply="isReplying = !isReplying"
        />

        <!-- Reply box -->
        <div v-if="isReplying">
            <comment-composer
                @post-cancel="isReplying = false"
            />
        </div>
    </section>    
</template>

<script>
import PostingActionsFooter from '@/components/PostingActionsFooter.vue';
import CommentComposer from '@/components/CommentComposer.vue';

export default {
    data () {
        return {
            isReplying: false,
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
        PostingActionsFooter,
        CommentComposer
    }
}
</script>

<style lang="scss">

</style>
