<template>
    <section class="card comment-card">
        <!--
            No title for comments, but we still put the author
            and a timestamp (which we'll make later)
        -->
        <header class="card-header">
            <router-link :to="postLink" class="card-header-title">
                {{ post.subject || "" }}
            </router-link>

            <router-link :to="authorLink"
                class="card-header-title is-size-7 has-text-right liblio-post-author">
                {{ by(post.user) }}
            </router-link>
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
            @action-like="onLike"
            @action-share="onShare"
            :postId="post.id"
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
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            isReplying: false,
        }
    },

    props: [
        'post'
    ],

    computed: {
        ...mapGetters([
            'myLikes', 'myShares', 'accessToken'
        ]),

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
        },

        onLike () {
            console.log(this.post.id);
            if (this.myLikes.indexOf(this.post.id) === -1) {
                this.$store.dispatch('likePost', {
                    postId: this.post.id,
                    token: this.accessToken
                });
            }
        },

        onShare () {
            if (this.myShares.indexOf(this.post.id) === -1) {
                this.$store.dispatch('sharePost', {
                    postId: this.post.id,
                    token: this.accessToken
                })
            }
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
