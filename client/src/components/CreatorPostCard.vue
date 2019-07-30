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
        <footer class="card-footer">
            <!-- Put actions (like, reply, etc.) here -->
        </footer>
    </section>
</template>

<script>
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
    }
}
</script>

<style lang="scss">
    .liblio-post-author {
        flex-grow: 0;
    }
</style>
