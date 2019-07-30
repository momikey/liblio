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
        <footer class="card-footer">
            <!-- Put actions (like, etc.) here -->
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
            return `by ${author}`;
        }
    }
}
</script>

<style lang="scss">
    // .comment-card {
    //     margin-bottom: 0.5rem;
    // }
</style>
