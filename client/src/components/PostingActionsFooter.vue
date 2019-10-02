<template>
    <footer class="card-footer">
        <!-- Put actions (like, etc.) here -->
        <span class="card-footer-item comment-actions">

            <b-tooltip :label="labels.reply" animated :delay="500">
                <b-button class="is-text"
                    @click="onReply"
                >
                    <b-icon icon="reply" />
                </b-button>
            </b-tooltip>

            <b-tooltip :label="labels.share" animated :delay="500">
                <b-button class="is-text"
                    @click="onShare"
                >
                    <b-icon icon="repeat" v-if="user && isPostShared(postId)"
                        class="is-shared-icon"
                    />
                    <b-icon icon="repeat" v-else />
                </b-button>
            </b-tooltip>

            <b-tooltip :label="labels.like" animated :delay="500">
                <b-button class="is-text"
                    @click="onLike"
                >
                    <b-icon icon="star" v-if="user && isPostLiked(postId)"
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
            }
        }
    },

    props: [
        'postId'
    ],

    computed: {
        ...mapGetters(
            ['isPostLiked', 'isPostShared', 'user']
        )
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
