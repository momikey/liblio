<template>
    <article class="card post-card" v-if="post">
        <!-- Post title -->
        <header class="card-header has-background-primary">
            <router-link :to="postLink" class="card-header-title has-text-primary-inverted">
                    {{ post.subject }}
            </router-link>

            <router-link :to="authorLink"
                class="card-header-title is-size-7 has-text-right liblio-post-author has-text-primary-inverted">
                {{ by(post.user) }}
            </router-link>
        </header>

        <!-- Link to parent post, if it exists -->
        <div v-if="post.parent_id" class="parent-link-container">
            <b-icon icon="reply" custom-class="mdi-flip-h" />
            <router-link :to="parentLink" class="parent-link">{{ labels.parent }}</router-link>
        </div>

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
            :postId="post.id"
        />

        <!-- Reply box -->
        <div v-if="isReplying">
            <comment-composer
                @post-cancel="isReplying = false"
            />
        </div>
    </article>
</template>

<script>
import PostingActionsFooter from '@/components/PostingActionsFooter.vue';
import CommentComposer from '@/components/CommentComposer.vue';

export default {
    data () {
        return {
            isReplying: false,

            labels: {
                parent: "Parent post"
            }
        }
    },

    props: [
        'post'
    ],

    computed: {
        postLink () {
            return `/web/post/${this.post.id}`;
        },

        authorLink () {
            return `/web/user/${this.post.user.id}`;
        },

        parentLink () {
            return `/web/post/${this.post.parent_id}`;
        }
    },

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

    .parent-link-container {
        margin: 8px 1rem 0 1rem;
        display: flex;
        justify-items: center;
    }

    .parent-link {
        padding-left: 6px;
    }
</style>
