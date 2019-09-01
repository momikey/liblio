<template>
    <section class="card">
        <div class="card-content has-text-left">
            <h1 class="title is-4">{{ user.display_name || '(' + user.username + ')' }}</h1>
            <p class="subtitle is-6">{{ actorAddress(user.username, user.origin) }}</p>
            <tag-list
                :tags="user.tags"
                align="left"
            />
            <p class="content">{{ user.bio }}</p>
        </div>
    </section>
</template>

<script>
import TagList from "@/components/TagList.vue";

import { actorAddress } from "@/modules/uri";

export default {
    props: [
        'user'
    ],

    methods: {
        actorAddress,
    },

    components: {
        TagList
    }
}
</script>

<style>

</style>
