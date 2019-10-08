<template>
    <section class="admin-main-panel">
        <h1 v-if="mode == 'all'">All users</h1>
        <h1 v-else>Local users</h1>
    </section>
</template>

<script>
export default {
    data () {
        return {

        }
    },

    props: [
        'mode'
    ]
}
</script>
