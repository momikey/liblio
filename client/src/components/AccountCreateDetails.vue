<template>
    <section class="account-create card">
        <form action="" class="card-content" name="account-create" target="_self">
            <p class="subtitle">{{ labels.header }}</p>

            <b-field horizontal :label="labels.username"
                :type="(usernameValid ? 'is-success' : '')"
            >
                <b-input name="username" expanded required
                    v-model="account.username"
                />
            </b-field>

            <b-field horizontal :label="labels.displayName">
                <b-input name="displayName" expanded
                    v-model="account.displayName"
                />
            </b-field>

            <b-field horizontal :label="labels.email">
                <b-input name="email" expanded required
                    type="email"
                    v-model="account.email"
                />
            </b-field>

            <b-field horizontal :label="labels.password">
                <b-input name="password" expanded required
                    type="password" password-reveal
                    v-model="account.password"
                />
            </b-field>

            <b-field horizontal :label="labels.retype"
                    :type="passwordsMatch"
                    :message="passwordMatchMessage"
            >
                <b-input name="retype" expanded required
                    type="password" password-reveal
                    v-model="retypePassword"
                />
            </b-field>

            <b-field class="level">
                <div class="level-item">
                    <b-button class="is-primary create-account-button"
                        :disabled="!canContinue"
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
            account: {
                username: '',
                displayName: '',
                email: '',
                password: ''
            },

            retypePassword: '',

            labels: {
                header: "Create your account",
                username: "Username",
                displayName: "Display name",
                email: "Email address",
                password: "Password",
                retype: "Retype password",
                next: "Next",
                cancel: "Cancel",

                passwordMatch: "Passwords match",
                passwordMismatch: "Passwords must match",
                noPassword: "You must enter a password"
            }
        }
    },

    computed: {
        passwordsMatch () {
            if (this.account.password == '' || this.retypePassword == '') {
                return '';
            } else if (this.account.password == this.retypePassword) {
                return 'is-success';
            } else {
                return 'is-danger';
            }
        },

        passwordMatchMessage () {
            if (this.passwordsMatch == 'is-success') {
                return this.labels.passwordMatch;
            } else if (!this.account.password) {
                return this.labels.noPassword;
            } else {
                return this.labels.passwordMismatch;
            }
        },

        usernameValid () {
            // TODO: Maybe check the server to see if the name is valid?
            // That can lead to attacks, though...
            return this.account.username != '' && this.account.username.length <= 64;
        },

        canContinue () {
            return (this.usernameValid && this.passwordsMatch == 'is-success' &&
                /.+@.+/.test(this.account.email));
        }
    },

    methods: {
        onNext () {
            this.$emit('next-step', this.account);
        },

        onCancel () {
            this.$emit('cancel-step');
        }
    }
}
</script>

<style lang="scss">
    .create-account-button {
        margin-left: 12px;
        margin-right: 12px;
        padding-left: 12px;
        padding-right: 12px;
        min-width: 8rem;
    }
</style>
