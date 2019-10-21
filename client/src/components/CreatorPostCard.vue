<template>
    <article class="card post-card" v-if="post">
        <!-- Post title -->
        <header class="card-header has-background-primary">
            <router-link :to="postLink" class="card-header-title has-text-primary-inverted">
                    {{ post.subject }}
            </router-link>

            <div class="post-metadata">
                <span class="post-date card-header-title is-size-7 has-text-primary-inverted">
                    {{ dateToNow(post.timestamp) }}
                </span>
                <span>
                    <router-link :to="authorLink"
                        class="card-header-title is-size-7 has-text-right has-text-primary-inverted liblio-post-author">
                        {{ by(post.user) }}
                    </router-link>
                </span>
            </div>
        </header>

        <!-- Link to parent post, if it exists -->
        <div v-if="post.parent_id" class="parent-link-container">
            <b-icon icon="reply" custom-class="mdi-flip-h" />
            <router-link :to="parentLink" class="parent-link">{{ labels.parent }}</router-link>
        </div>

        <!-- Post images, if available -->
        <div v-if="images" class="post-image-container">
            <figure v-for="image in images" :key="image.uri" class="image is-128x128">
                <!-- TODO: Descriptive text for images, for accessibility reasons -->
                <img :src="image.uri" class="thumbnail" :alt="image.uri" />
            </figure>
        </div>

        <!-- Main post content -->
        <div class="card-content">
            <div class="content">

                <!-- TODO: sanitize, format, etc. -->
                {{ post.content }}
            </div>
        </div>

        <!-- Post attachments -->
        <div class="post-attachments">
            <b-tag v-for="file in attachments" :key="file.uri">
                <a :href="file.uri" target="_blank">{{ file.uri }}</a>
            </b-tag>
        </div>

        <!-- Post actions -->
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
                @replied="isReplying = false"
                :parent="post"
            />
        </div>
    </article>
</template>

<script>
import PostingActionsFooter from '@/components/PostingActionsFooter.vue';
import CommentComposer from '@/components/CommentComposer.vue';
import { mapGetters } from 'vuex';
import { dateToNow } from "@/modules/post";

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
        },

        images () {
            return this.post.files.filter(e => e.type.startsWith('image'));
        },

        attachments () {
            // TODO: Break out into audio, video, etc.
            return this.post.files.filter(e => !e.type.startsWith('image'));
        }
    },

    methods: {
        dateToNow,

        by (author) {
            return `by ${author.username}`;
        },

        onLike () {
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
