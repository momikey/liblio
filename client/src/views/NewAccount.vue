<template>
    <div class="new-account columns">
        <div class="column is-two-thirds">
            <account-create
            />
        </div>
    </div>
</template>

<script>
import AccountCreate from '@/components/AccountCreate.vue';

export default {
    data () {
        return {

        }
    },

    components: {
        AccountCreate
    }
}
</script>

<style lang="scss">

</style>
