<template>
    <section class="account-create card">
        <form action="" class="card-content" name="account-create" target="_self">
            <p class="subtitle">{{ labels.header }}</p>

            <b-field>
                <div class="content" v-html="adminMessage" />
            </b-field>

            <b-field class="level">
                <div class="level-item">
                    <b-button class="is-primary create-account-button"
                        @click="onNext"
                    >
                        {{ labels.next }}
                    </b-button>
                </div>
            </b-field>
        </form>
    </section>
</template>

<script>
export default {
    data () {
        return {
            // TODO: Retrieve from the server, allowing admin customization.
            adminMessage: "<p>Welcome to Liblio! Enjoy yourself, and make something interesting!</p>",

            labels: {
                header: "Welcome to our community",

                next: "Continue to your dashboard"
            }
        }
    },

    methods: {
        onNext () {
            this.$emit('next-step');
        }
    }
}
</script>
