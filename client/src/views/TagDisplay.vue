<template>
    <div class="tag-display">
        <section class="box">
            <div class="tag-info">
                <h1 class="title"> {{ tag.name }} </h1>
                <p class="is-6"> {{ tag.description }} </p>
            </div>
        </section>

        <section class="card">
            <div class="card-content tag-users">
                <h1 class="subtitle">
                    {{ labels.usersHeader }}
                </h1>
            </div>
        </section>

        <section class="card">
            <div class="card-content tag-posts">
                <h1 class="subtitle">
                    {{ labels.postsHeader }}
                </h1>
            </div>
        </section>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    data () {
        return {
            // TODO: i18n
            labels: {
                usersHeader: "Users with this tag",
                postsHeader: "Posts with this tag"
            }
        }
    },

    props: [
        'tagname'
    ],

    computed: {
        tag () {
            return this.$store.getters.tag(this.tagname);
        }
    }
}
</script>

<style>
    .tag-display > section {
        margin: 1rem 0;
    }
</style>