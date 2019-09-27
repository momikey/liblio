<template>
    <div class="directory columns">
        <div class="column is-two-thirds" id="directory-column">
        <template v-if="tags.length">
            <div class="tag-entry" v-for="tag in tags" :key="tag.name">
                <h1 class="title">{{ tag.name }}</h1>
                <p>{{ tag.description }}</p>
            </div>
        </template>

        <template v-else>
            <p>{{ labels.noTags }}</p>
        </template>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    data () {
        return {
            // TODO: i18n
            labels: {
                noTags: "No tags defined on this server"
            }
        }
    },

    computed: {
        ...mapGetters(['tags'])
    },

    mounted () {
        this.$store.dispatch('getTagList')
        console.log(this.$store.getters.tags)
    }
}
</script>