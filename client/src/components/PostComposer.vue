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
                <div class="is-pulled-right">
                <b-button @click="onPost" class="">Post</b-button>
                <b-button @click="onClear" class="">Clear</b-button>
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

            // Labels (TODO: Localization)
            labels: {
                subject: "Subject",
                message: "Message",

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
                console.log(`Posting with subject ${this.post.subject} and body ${this.post.body}`);
            } else {
                this.notifyError(this.labels.errors.noPostBody);
            }
        },

        onClear () {
            this.post.subject = '';
            this.post.body = '';
        },

        notifyError (error) {
            this.$notification.open({
                type: 'is-danger',
                message: error,
                autoClose: true,
                position: 'is-bottom-left'
            })
        }
    }
}
</script>

<style lang="scss">
    .composer {
        margin-bottom: 1rem;
    }

    .composer-actions {
        padding-bottom: 2rem;
    }
</style>
