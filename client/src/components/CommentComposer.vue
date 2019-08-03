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

                    <b-button @click="onClear" class="">
                        Clear
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

    methods: {
        onPost () {
            if (this.post.body) {
                console.log(`Posting comment ${this.post.body}`);
            } else {
                this.notifyError(this.labels.errors.commentEmpty);
            }
        },

        onClear () {
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

</style>
