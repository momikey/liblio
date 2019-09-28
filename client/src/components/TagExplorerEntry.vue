<template>
    <section class="card">
        <div class="card-content has-text-left">
            <h1 class="title">
                <router-link :to="tagLink(tag)">
                    #{{ tag.name }}
                </router-link>
            </h1>
            <p class="is-6">
                {{ tag.description }}
            </p>
        </div>
    </section>
</template>

<script>
import { uriForTag } from "../modules/uri";

export default {
    props: [
        'tag'
    ],

    methods: {
        uriForTag,

        tagLink (tag) {
            return `/web/tag/${this.tag.name}`;
        }
    }
}
</script>