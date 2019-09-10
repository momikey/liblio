<template>
    <section class="card post-card" v-if="post">
        <!-- Post title -->
        <header class="card-header has-background-primary">
            <p class="card-header-title has-text-primary-inverted">
                {{ post.subject }}
            </p>

            <p class="card-header-title is-size-7 has-text-right liblio-post-author has-text-primary-inverted">
                {{ by(post.user) }}
            </p>
        </header>

        <!-- Post image, if available -->
        <div v-if="post.image" class="card-image">
            <figure class="image">
                <!-- Put image here -->
            </figure>
        </div>

        <!-- Main post content -->
        <div class="card-content">
            <div class="content">


                <!-- TODO: sanitize, format, etc. -->
                {{ post.content }}
            </div>
        </div>

        <!-- Post actions -->
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
            return `by ${author.username}`;
        }
    },

    components: {
        PostingActionsFooter,
        CommentComposer
    },
}
</script>

<style lang="scss">
    .liblio-post-author {
        flex-grow: 0;
    }
</style>
