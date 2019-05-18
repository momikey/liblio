<template>
    <section id="creator-panel" class="section">
        <div class="container is-fluid">
            <div class="level">
                <!-- User avatar -->
                <div class="level-item">
                    <figure class="image is-128x128" id="avatar-figure">
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

            <div class="level">
                <!-- User tags -->
                <div class="level-item">
                    <b-tag rounded
                        v-for="tag in tags" :key="tag.key">
                        <router-link :to="uriForTag(tag.key)">{{ tag.value }}</router-link>
                    </b-tag>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
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

    methods: {
        uriForTag (key) {
            return `tag/${key}`;
        }
    }
}
</script>

<style lang="scss" scoped>
#creator-panel {
    background-color: #ffeedd;
    height: 100%;
    padding-top: 32px;
}

#avatar-figure > img {
    background-color: gray;
}
</style>
