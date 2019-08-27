<template>
    <div class="home columns">
        <div class="column is-two-thirds">
        </div>

        <div class="column is-one-third">
            <creator-panel />
        </div>
    </div>
</template>

<script>
    import CreatorPanel from '@/components/CreatorPanel.vue'

    export default {
        name: 'home',

        components: {
            CreatorPanel,
        },

        data () {
            return {
                testUser: null,
            }
        },

        mounted () {

        }
    }
</script>
