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
                    <h1 class="is-size-4">{{ username }}</h1>
                    <h2 class="is-size-6">({{ formatAddress() }})</h2>
                    </div>
                </div>
            </div>

            <!-- User tags - this component is already in a level -->
            <tag-list
                :tags="tags"
            />

            <div class="create-buttons">
                <b-button icon-left="plus" class="is-primary create-button"
                    tag="router-link" to="/web/new-post" append
                >
                    {{ labels.newPost }}
                </b-button>

                <b-button icon-left="plus" class="is-primary create-button"
                    tag="router-link" to="/web/new-announcement" append
                >
                    {{ labels.newAnnouncement }}
                </b-button>
            </div>
        </div>
    </section>
</template>

<script>
import { actorAddress } from "@/modules/uri";

import TagList from "@/components/TagList.vue";
import { mapGetters } from 'vuex';
    
export default {
    data () {
        return {
            labels : {
                noName: '(no name given)',
                newPost: 'Make a post',
                newAnnouncement: 'Show off your work'
            },

            tags: [
                { key: 'test', value: "Tester" },
                { key: 'author', value: "Author" }
            ]
        }
    },

    computed: {
        ...mapGetters({
            'user': 'myProfile'
        }),

        username () {
            return this.user.display_name || this.labels.noName;
        }
    },

    methods: {
        formatAddress () {
            return actorAddress(this.$store.getters.user, this.user.origin);
        }
    },

    mounted () {
        if (this.user) {
            this.$store.dispatch('getProfile');
            this.$store.dispatch('getMyInfo');
        }
    },

    components: {
        TagList
    }
}
</script>

<style lang="scss">
    .creator-avatar-figure > img {
        background-color: gray;
    }

    .create-buttons {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .create-button {
        margin: 8px auto;
    }
</style>
