<template>
    <div class="new-account container">
        <account-create
        />
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
    .new-account.container {
        max-width: 960px;
    }
</style>
