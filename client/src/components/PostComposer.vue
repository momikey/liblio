<template>
    <section class="composer card">
        <div class="card-content">
            <b-field horizontal :label="labels.subject">
                <b-input
                    v-model="post.subject"
                    :placeholder="labels.placeholders.subject"
                />
            </b-field>

            <b-field horizontal :label="labels.message">
                <b-input
                    v-model="post.body"
                    :placeholder="labels.placeholders.message"
                    type="textarea"
                />
            </b-field>

            <div class="composer-actions">
                <div class="is-pulled-left">
                    <b-field class="file">
                        <b-upload v-model="uploads"
                            multiple
                            name="uploads"
                        >
                            <a
                                class="button is-primary"
                            >
                                <span>{{ labels.upload }}</span>
                                <b-icon icon="upload" />
                            </a>
                        </b-upload>
                        <template v-if="uploads.length">
                            <span class="file-name">
                                {{ uploads.length }} upload(s)
                            </span>
                            <b-dropdown class="is-pulled-right" position="is-bottom-left">
                                <b-icon icon="dots-vertical" slot="trigger" />
                                <b-dropdown-item v-for="file in uploads" :key="file.name"
                                    class="columns" custom
                                >
                                    <span class="column dropdown-filename">{{ file.name }}</span>
                                    <span class="column is-narrow">
                                        <a
                                            class="has-text-main"
                                            @click="removeFile(file)"
                                        >
                                            <b-icon icon="delete" />
                                        </a>
                                    </span>
                                </b-dropdown-item>
                                <b-dropdown-item custom
                                    class="columns level"
                                >
                                    <a class="has-text-main level-item dropdown-clearall"
                                        @click="uploads = []"
                                    >
                                        Clear uploads
                                    </a>
                                </b-dropdown-item>
                            </b-dropdown>
                        </template>
                    </b-field>
                </div>
                <div class="is-pulled-right">
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
        </div>
    </section>
</template>

<script>
export default {
    data () {
        return {
            // Post data
            post: {
                subject: '',
                body: '',
                tags: []
            },

            // This post's uploads, if any
            uploads: [],

            // Labels (TODO: Localization)
            labels: {
                subject: "Subject",
                message: "Message",
                post: "Post",
                clear: "Clear",
                upload: "Upload",

                placeholders: {
                    subject: "Announcing...",
                    message: "This is what I'm doing..."
                },

                errors: {
                    noPostBody: "You must type a message"
                }
            }
        }
    },

    methods: {
        onPost () {
            if (this.post.body) {
                this.$emit('post-created', {
                    subject: this.post.subject,
                    body: this.post.body,
                    tags: this.post.tags,
                    uploads: this.uploads.length ? this.uploads : undefined
                })
            } else {
                this.notifyError(this.labels.errors.noPostBody);
            }
        },

        onClear () {
            this.post.subject = '';
            this.post.body = '';
            this.uploads = [];
        },

        notifyError (error) {
            this.$notification.open({
                type: 'is-danger',
                message: error,
                autoClose: true,
                position: 'is-bottom-left'
            })
        },

        removeFile (file) {
            this.uploads.splice(this.uploads.indexOf(file), 1);
        }
    }
}
</script>

<style lang="scss">
    .composer {
        margin-bottom: 1rem;
        margin-top: 4px;
    }

    .composer-actions {
        padding-bottom: 2rem;
    }

    .dropdown-clearall {
        padding-bottom: 0.75rem;
    }
</style>
