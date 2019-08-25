<template>
    <section class="account-create card">
        <form action="" class="card-content" name="account-create" target="_self">
            <p class="subtitle">{{ labels.header }}</p>

            <b-field>
                <b-input type="textarea" rows="5" v-model="rules" readonly
                />
            </b-field>

            <b-field class="level">
                <div class="level-item">
                    <b-button class="is-primary create-account-button"
                        @click="onNext"
                    >
                        {{ labels.next }}
                    </b-button>

                    <b-button class="create-account-button"
                        @click="onCancel"
                    >
                        {{ labels.cancel }}
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
            // TODO: Retrieve from the server, with lots of customization
            rules: "Be nice and have fun!",

            labels: {
                next: "I agree",
                cancel: "Cancel",

                header: "Our rules"
            }
        }
    },

    methods: {
        onNext () {
            this.$emit('next-step');
        },

        onCancel() {
            this.$emit('cancel-step');
        }
    }
}
</script>
