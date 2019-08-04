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

            <b-tooltip :label="labels.announce" animated :delay="500">
                <b-button class="is-text"
                    @click="onAnnounce"
                >
                    <b-icon icon="repeat" />
                </b-button>
            </b-tooltip>

            <b-tooltip :label="labels.like" animated :delay="500">
                <b-button class="is-text"
                    @click="onLike"
                >
                    <b-icon icon="star-outline" />
                </b-button>
            </b-tooltip>
        </span>
    </footer>
</template>

<script>
export default {
    data () {
        return {
            labels: {
                reply: "Reply",
                announce: "Announce",
                like: "Like",
            }
        }
    },

    methods: {
        onReply () {
            this.$emit('action-reply');
        },

        onLike () {
            this.$emit('action-like');
        },

        onAnnounce () {
            this.$emit('action-announce');
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
