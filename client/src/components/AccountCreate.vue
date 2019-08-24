<template>
    <!--
        Acocunt creation steps:
        1. Create username/set password
        2. Set up profile
        3. Getting started (tutorial, etc.)
    -->
    <section class="account-create-wizard">
        <b-steps
            v-model="currentStep"
            :hasNavigation="false"
        >
            <b-step-item>
                <!-- Create an account on this server -->
                <account-create-details
                    @next-step="onCreateAccountStep"
                    @cancel-step="onCancelStep"
                />
            </b-step-item>

            <b-step-item>
                <!-- Set up your profile -->
            </b-step-item>

            <b-step-item>
                <!-- Do any post-creation tasks, such as showing a tutorial or admin message -->
            </b-step-item>
        </b-steps>
    </section>
</template>

<script>
import AccountCreateDetails from '@/components/AccountCreateDetails.vue';

export default {
    data () {
        return {
            currentStep: 0,

            account: null,
        }
    },

    methods: {
        onCreateAccountStep (account) {
            // We don't actually create the account on the server in this step,
            // because the user might cancel the creation in the profile step.
            // So we just save the credentials for the moment, then use them if
            // we actually do have a new account.
            console.log(account);

            this.account = account;
            ++this.currentStep;
        },

        onCancelStep () {
            if (this.currentStep > 0) {
                --this.currentStep;
            } else {
                this.$router.back();
            }
        }
    },

    components: {
        AccountCreateDetails
    }
}
</script>
