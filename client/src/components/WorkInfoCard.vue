<template>
    <section class="card work-info-card">
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

                <!-- URL -->
                <div class="work-url">
                    <hr />
                    <a :href="url">Check it out!</a>
                    <hr />
                </div>

                <!-- Tags -->
                <tag-list
                    :tags="tags"
                    align="left"
                />
            </div>
        </div>
    </section>
</template>

<script>
import TagList from "@/components/TagList.vue"

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

    components: {
        TagList
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
