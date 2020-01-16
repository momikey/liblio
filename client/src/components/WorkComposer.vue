<template>
    <section class="composer work-composer card">
        <div class="card-content">
            <b-field horizontal :labels="labels.subject">
                <b-input
                    v-model="post.subject"
                    :placeholder="labels.placeholders.subject"
                />
            </b-field>

            <b-field horizontal :labels="labels.link">
                <b-input
                    v-model="post.link"
                    :placeholder="labels.placeholders.link"
                />
            </b-field>

            <!-- TODO: Optional post image -->

            <b-field horizontal :labels="labels.body">
                <b-input
                    v-model="post.body"
                    :placeholder="labels.placeholders.body"
                    type="textarea"
                />
            </b-field>

            <div class="composer-actions">
                <!-- TODO: File uploads, tags, etc. -->
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

            uploads: [],

            labels: {
                subject: "Subject",
                link: "Link",
                body: "Message body",

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

    methods: {

    }
}
</script>

<style lang="scss">

</style>