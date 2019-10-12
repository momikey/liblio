<template>
    <div class="home columns">
        <div class="column is-one-third">
            <creator-panel v-if="user"
            />

            <login-panel v-else
            />
        </div>
        
        <div class="column is-two-thirds">
            <router-view />
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    import CreatorPanel from '@/components/CreatorPanel.vue';
    import LoginPanel from '@/components/LoginPanel.vue';

    export default {
        name: 'home',

        data () {
            return {
            }
        },

        computed: {
            ...mapGetters([
                'user'
            ])
        },

        mounted () {

        },

        components: {
            CreatorPanel,
            LoginPanel
        }
    }
</script>
