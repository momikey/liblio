<template>
    <section class="side-panel section">
        <div class="container is-fluid">
            <div class="level">
                <!-- User avatar -->
                <div class="level-item">
                    <figure class="image is-128x128 creator-avatar-figure">
                        <img class="is-rounded" src="../assets/logo.png" />
                    </figure>
                </div>
            </div>

            <div class="level">
                <!-- User name -->
                <div class="level-item has-text-centered">
                    <div>
                    <h1 class="is-size-4">Your name here</h1>
                    <h2 class="is-size-6">(@yourname@example.com)</h2>
                    </div>
                </div>
            </div>

            <!-- User tags - this component is already in a level -->
            <tag-list
                :tags="tags"
            />
        </div>
    </section>
</template>

<script>
import TagList from "@/components/TagList.vue";
    
export default {
    data () {
        return {
            tags: [
                { key: 'test', value: "Tester" },
                { key: 'author', value: "Author" }
            ]
        }
    },

    props: [
        'user'
    ],

    components: {
        TagList
    }
}
</script>

<style lang="scss">
    .creator-avatar-figure > img {
        background-color: gray;
    }
</style>
