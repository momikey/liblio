<template>
    <section class="card">
        <!-- Work title -->
        <header class="card-header">
            <p class="card-header-title is-centered title is-4">
                {{ title }}
            </p>
        </header>

        <!-- Optional image -->
        <div v-if="image" class="card-image">
            <figure class="image">
                <!-- Put image here -->
            </figure>
        </div>

        <!-- Main content -->
        <div class="card-content">
            <div class="container is-fluid">
                <!-- Description -->
                <div class="work-description" v-html="description" />

                <!-- Tags -->
                <div class="level">
                    <div class="level-item">
                        <b-tag rounded
                            v-for="tag in tags" :key="tag.key">
                            <router-link :to="uriForTag(tag.key)">{{ tag.value }}</router-link>
                        </b-tag>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { uriForTag } from "@/modules/uri";

export default {
    data () {
        return {

        }
    },

    props: [
        'title',
        'image',
        'description',
        'url',
        'tags'
    ],

    methods: {
        uriForTag
    }
}

</script>

<style lang="scss">
    .work-description {
        text-align: justify;
    }

    .work-description p {
        margin-bottom: 1rem;
    }
</style>
