<template>
    <div class="home columns">
        <div class="column is-two-thirds">
        </div>

        <div class="column is-one-third">
            <creator-panel v-if="user"
            />

            <login-panel v-else
            />
        </div>
    </div>
</template>

<script>
    import CreatorPanel from '@/components/CreatorPanel.vue';
    import LoginPanel from '@/components/LoginPanel.vue';

    export default {
        name: 'home',

        data () {
            return {
                user: null,
            }
        },

        mounted () {

        },

        components: {
            CreatorPanel,
            LoginPanel
        }
    }
</script>
