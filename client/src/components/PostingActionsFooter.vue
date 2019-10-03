<template>
    <footer class="card-footer">
        <!-- Put actions (like, etc.) here -->
        <span class="card-footer-item comment-actions">

            <b-tooltip :label="user ? labels.reply : labels.loginReply" animated :delay="500">
                <b-button class="is-text"
                    @click="onReply"
                    :disabled="!user"
                >
                    <b-icon icon="reply" />
                </b-button>
            </b-tooltip>

            <b-tooltip :label="user ? labels.share : labels.loginShare" animated :delay="500">
                <b-button class="is-text"
                    @click="onShare"
                    :disabled="!user"
                >
                    <b-icon icon="repeat" v-if="shared"
                        class="has-text-shared-icon"
                    />
                    <b-icon icon="repeat" v-else />
                </b-button>
            </b-tooltip>

            <b-tooltip :label="user ? labels.like : labels.loginLike" animated :delay="500">
                <b-button class="is-text"
                    @click="onLike"
                    :disabled="!user"
                >
                    <b-icon icon="star" v-if="liked"
                        class="has-text-liked-icon"
                    />
                    <b-icon icon="star-outline" v-else />
                </b-button>
            </b-tooltip>
        </span>
    </footer>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            labels: {
                reply: "Reply",
                share: "Share",
                like: "Like",
                loginReply: "Log in to reply",
                loginShare: "Log in to share",
                loginLike: "Log in to like"
            }
        }
    },

    props: [
        'postId'
    ],

    computed: {
        ...mapGetters(
            ['isPostLiked', 'isPostShared', 'user']
        ),

        liked () {
            return this.user && this.isPostLiked(this.postId);
        },

        shared () {
            return this.user && this.isPostShared(this.postId);
        }
    },

    methods: {
        onReply () {
            this.$emit('action-reply');
        },

        onLike () {
            this.$emit('action-like');
        },

        onShare () {
            this.$emit('action-share');
        }
    }
}
</script>

<style lang="scss">
    .comment-actions button {
        margin-left: 2rem;
        margin-right: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

</style>
