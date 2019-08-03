<template>
    <section class="card post-card">
        <!-- Post title -->
        <header class="card-header has-background-primary">
            <p class="card-header-title has-text-primary-inverted">
                {{ post.title }}
            </p>

            <p class="card-header-title is-size-7 has-text-right liblio-post-author has-text-primary-inverted">
                {{ by(post.author) }}
            </p>
        </header>

        <!-- Post image, if available -->
        <div v-if="post.iamge" class="card-image">
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
            return `by ${author}`
        }
    },

    components: {
        PostingActionsFooter
    }
}
</script>

<style lang="scss">
    .liblio-post-author {
        flex-grow: 0;
    }
</style>
