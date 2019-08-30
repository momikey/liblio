<template>
    <!--
        Acocunt creation steps:
        1. ToS, rules, etc.
        2. Create username/set password
        3. Set up profile
        4. Review the info
        5. Welcome!
    -->
    <section class="account-create-wizard container">
        <b-steps
            v-model="currentStep"
            :hasNavigation="false"
        >
            <b-step-item>
                <!-- Show the server's rules and get the user's agreement -->
                <account-create-rules
                    @next-step="onAcceptRules"
                    @cancel-step="onCancelStep"
                />
            </b-step-item>

            <b-step-item>
                <!-- Create an account on this server -->
                <account-create-details
                    @next-step="onCreateAccountStep"
                    @cancel-step="onCancelStep"
                />
            </b-step-item>

            <b-step-item>
                <!-- Set up your profile -->
                <account-create-profile
                    @next-step="onCreateProfileStep"
                    @previous-step="onCancelStep"
                />
            </b-step-item>

            <b-step-item>
                <!-- Review your account info -->
                <account-create-review
                    :account="account"
                    :profile="profile"
                    @next-step="onAccountReviewed"
                    @previous-step="onCancelStep"
                />
            </b-step-item>

            <b-step-item>
                <!-- Do any post-creation tasks, such as showing a tutorial or admin message -->
                <account-create-welcome
                    @next-step="onCreationComplete"
                />
            </b-step-item>
        </b-steps>
    </section>
</template>

<script>
import AccountCreateRules from '@/components/AccountCreateRules.vue';
import AccountCreateDetails from '@/components/AccountCreateDetails.vue';
import AccountCreateProfile from '@/components/AccountCreateProfile.vue';
import AccountCreateReview from '@/components/AccountCreateReview.vue';
import AccountCreateWelcome from '@/components/AccountCreateWelcome.vue';

export default {
    data () {
        return {
            currentStep: 0,

            account: null,
            profile: null
        }
    },

    methods: {
        onAcceptRules () {
            // The user has agreed to the server's terms of use, and can
            // now continue with the account creation process.
            // TODO: Do we need to worry about GDPR, etc.?

            ++this.currentStep;
        },

        onCreateAccountStep (account) {
            // We don't actually create the account on the server in this step,
            // because the user might cancel the creation in the profile step.
            // So we just save the credentials for the moment, then use them if
            // we actually do have a new account.

            this.account = account;
            ++this.currentStep;
        },

        onCreateProfileStep (profile) {
            // After this step, we haven't yet submitted the data to the server,
            // because we want to give the user one last chance to review and
            // possibly back out.

            this.profile = profile;
            ++this.currentStep;
        },

        onAccountReviewed () {
            // The user has reviewed the account and profile details, and is now
            // submitting them to the server.
            
            this.$store.dispatch('createAccount', {
                account: this.account,
                profile: this.profile}
            )
            ++this.currentStep;
        },

        onCreationComplete () {
            // At this point, the user has created an account and started a profile.
            // All that's left is a redirect to either the login page or the dashboard.
            // Which one we use can be decided later. (TODO: Do that.)

            // TODO: Make this go to the right location.
            this.$router.push('/');
        },

        onCancelStep () {
            // "Cancel" goes back a step, but *not* to the initial page, since
            // that's the ToS page.
            if (this.currentStep > 1) {
                --this.currentStep;
            } else {
                this.$router.back();
            }
        }
    },

    components: {
        AccountCreateRules,
        AccountCreateDetails,
        AccountCreateProfile,
        AccountCreateReview,
        AccountCreateWelcome
    }
}
</script>
