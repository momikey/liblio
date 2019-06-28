<template>
    <section class="card">
        <div class="card-content has-text-left">
            <h1 class="title is-4">{{ user.name }}</h1>
            <p class="subtitle is-6">{{ user.address }}</p>
            <tag-list
                :tags="user.tags"
                align="left"
            />
        </div>
    </section>
</template>

<script>
import TagList from "@/components/TagList.vue";

export default {
    props: [
        'user'
    ],

    components: {
        TagList
    }
}
</script>

<style>

</style>
