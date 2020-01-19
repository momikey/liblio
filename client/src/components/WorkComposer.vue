<template>
    <section class="composer work-composer card">
        <div class="card-content">
            <b-field :label="labels.subject" label-position="inside">
                <b-input
                    v-model="post.subject"
                    :placeholder="labels.placeholders.subject"
                />
            </b-field>

            <b-field :label="labels.link" label-position="inside">
                <b-input
                    v-model="post.link"
                    :placeholder="labels.placeholders.link"
                />
            </b-field>

            <!-- TODO: Optional post image -->
            <b-field class="file cover-uploader" grouped position="is-centered">
                <template v-if="!cover">
                    <b-upload v-model="cover"
                        name="cover"
                        accept="image/*"
                        class="cover-image-uploader"
                    >
                        <a
                            class="button is-primary"
                        >
                            <span>{{ labels.cover }}</span>
                            <b-icon icon="upload" />
                        </a>
                    </b-upload>
                </template>

                <template v-else>
                    <div class="cover-image-container">
                        <figure class="image is-128x128">
                            <!-- TODO: Descriptive text for images, for accessibility reasons -->
                            <img :src="coverUri" class="thumbnail" :alt="labels.coverUri" />
                        </figure>
                        <b-button type="is-danger"
                            icon-right="delete"
                            @click="clearCoverImage"
                        />
                    </div>
                </template>
            </b-field>

            <b-field>
                <b-input
                    v-model="post.body"
                    :placeholder="labels.placeholders.body"
                    type="textarea"
                    rows="10"
                />
            </b-field>

            <hr />

            <div class="composer-actions">
                <!-- TODO: File uploads, tags, etc. -->
                <b-button
                    @click="onPost"
                    :disabled="!post.body.length"
                    icon-left="email"
                    :class="post.body.length ? 'is-primary' : false"
                >
                    {{ labels.post }}
                </b-button>

                <b-button @click="onClear" class="">
                    {{ labels.clear }}
                </b-button>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    data () {
        return {
            post: {
                subject: '',
                link: '',
                body: ''
            },

            cover: null,
            uploads: [],

            labels: {
                subject: "Subject",
                link: "Link",
                body: "Message body",
                cover: "Upload a cover image",
                coverUri: "Cover image",
                post: "Post",
                clear: "Clear",

                placeholders: {
                    subject: "Here's what I'm working on",
                    link: "https://example.com/my-greatest-work",
                    body: "Tell the world about your creation."
                },

                errors: {

                }
            }
        }
    },

    computed: {
        coverUri () {
            return URL.createObjectURL(this.cover);
        }
    },

    methods: {
        clearCoverImage () {
            this.cover = null;
        },

        onPost () {

        },

        onClear () {
            this.post.subject = '';
            this.post.link = '';
            this.post.body = '';
            this.cover = null;
            this.uploads = [];
        }
    }
}
</script>

<style lang="scss">
    .cover-image-container {
        display: flex;
        align-items: top;
    }

    .cover-uploader {
        min-height: 128px;
    }

    .cover-uploader label {
        margin-top: auto;
        margin-bottom: auto;
    }
</style>