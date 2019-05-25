<template>
    <section class="card">
        <div class="card-content has-text-left">
            <h1 class="title is-4">{{ user.name }}</h1>
            <p class="subtitle is-6">{{ user.address }}</p>
        </div>
    </section>
</template>

<script>
export default {
    props: [
        'user'
    ]
}
</script>

<style>

</style>
