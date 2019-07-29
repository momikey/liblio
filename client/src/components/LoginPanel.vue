<template>
    <section class="login-panel card">
        <div class="card-content">
            <p class="title">{{ labels.header }}</p>

            <b-field :label="labels.username">
                <b-input v-model="login.username" />
            </b-field>

            <b-field :label="labels.password">
                <b-input v-model="login.password"
                    type="password"
                />
            </b-field>

            <b-field class="remember">
                <b-checkbox v-model="login.remember">{{ labels.remember }}</b-checkbox>
            </b-field>

            <b-field class="level">
                <b-button
                    class="level-item login-panel-button"
                    type="is-primary"
                    @click="onLogin"
                >
                    {{ labels.loginButton }}
                </b-button>

                <b-button
                    class="level-item login-panel-button"
                    @click="onClear"
                >
                    {{ labels.clearButton }}
                </b-button>
            </b-field>
        </div>
    </section>
</template>

<script>
export default {
    data () {
        return {
            login: {
                username: '',
                password: '',
                remember: false,
            },

            labels: {
                header: "Log in to Liblio",
                username: "Username",
                password: "Password",
                remember: "Remember me",
                loginButton: "Log in",
                clearButton: "Clear"
            }
        }
    },

    methods: {
        onLogin () {
            for (const k of Object.keys(this.login)) {
                console.log(`${k} = ${this.login[k]}`);
            }
        },

        onClear () {
            this.login.username = '';
            this.login.password = '';
            this.login.remember = false;
        }
    }
}
</script>

<style lang="scss" scoped>
    .login-panel-button {
        margin-left: 12px;
        margin-right: 12px;
    }

    .remember {
        text-align: left;
        padding-left: 12px;
        margin-top: 24px;
    }
</style>
