<template>
    <section class="account-create card">
        <form action="" class="card-content" name="account-create" target="_self">
            <p class="subtitle">{{ labels.header }}</p>

            <p>{{ labels.explanation }}</p>

            <div class="box account-review">
                <table>
                    <tr v-for="row in accountReviewData" :key="row.key">
                        <td class="account-review-label">{{ row.label }}</td>
                        <td class="account-review-value">{{ row.value }}</td>
                    </tr>
                </table>

                <table>
                    <tr v-for="row in profileReviewData" :key="row.key">
                        <td class="account-review-label">{{ row.label }}</td>
                        <td class="account-review-value">{{ row.value || labels.noText }}</td>
                    </tr>
                </table>
            </div>

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
            labels: {
                header: "Review your details",

                explanation: `Take a moment to review the information you have provided.
                If everything is correct, click or tap the "Create Account" button to join
                our community.`,

                next: "Create Account",
                cancel: "Back",

                noText: "(not given)",

                accountReview: {
                    'username': "Username",
                    'email': "Email address"
                },

                profileReview: {
                    'name': "Display name",
                    'role': "Role",
                    'bio': "Description"
                }
            },
        }
    },

    props: [
        'account',
        'profile'
    ],

    computed: {
        accountReviewData () {
            if (this.account) {
                return [
                    { key: 'username', label: this.labels.accountReview.username, value: this.account.username },
                    { key: 'email', label: this.labels.accountReview.email, value: this.account.email }
                ]
            } else {
                return [];
            }
        },

        profileReviewData () {
            if (this.profile) {
                return [
                    { key: 'name', label: this.labels.profileReview.name, value: this.profile.name },
                    { key: 'role', label: this.labels.profileReview.role, value: this.profile.role },
                    { key: 'bio', label: this.labels.profileReview.bio, value: this.profile.bio }
                ]
            } else {
                return [];
            }
        }
    },

    methods: {
        onNext () {
            this.$emit('next-step');
        },

        onCancel () {
            this.$emit('previous-step');
        }
    }
}
</script>

<style lang="scss">
    .account-review {
        margin-top: 1rem;
    }

    .account-review table {
        width: 90%;
        margin: auto;
    }

    .account-review table:nth-of-type(2) {
        border-top-style: solid;
        border-width: 1px;
        border-color: gray;
    }

    .account-review table tr {
        width: 48%;
        line-height: 2.5;
    }

    .account-review table tr td:nth-of-type(2) {
        text-align: right;
    }
</style>
