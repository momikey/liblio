<template>
    <section class="composer card">
        <div class="card-content">
            <b-field>
                <b-input
                    v-model="post.body"
                    :placeholder="labels.message"
                    type="textarea"
                />
            </b-field>

            <div class="composer-actions">
                <div class="is-pulled-right">
                    <b-button
                        @click="onPost"
                        :disabled="!post.body.length"
                        icon-left="email"
                    >
                        Submit
                    </b-button>

                    <b-button @click="onCancel" class="">
                        Cancel
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
            post: {
                body: '',
            },

            // Placeholders (replace with localized strings later)
            labels: {
                message: "What's on your mind?",

                errors: {
                    commentEmpty: "Your comment cannot be blank",
                }
            }
        }
    },

    props: [
        'parent'
    ],

    methods: {
        onPost () {
            if (this.post.body) {
                let p = {
                    body: this.post.body,
                    parent: this.parent.id
                }

                if (this.parent.subject) {
                    p.subject = this.parent.subject;
                }

                this.$store.dispatch('newPost', {
                    post: p,
                    token: this.$store.getters.accessToken
                });

                this.$emit('replied');
            } else {
                this.notifyError(this.labels.errors.commentEmpty);
            }
        },

        onCancel () {
            this.post.body = '';
            this.$emit('post-cancel');
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
