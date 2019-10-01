<template>
    <post-composer class="post-composer"
        @post-created="onPostCreated"
    />
</template>

<script>
import PostComposer from "@/components/PostComposer.vue";
import { mapActions } from 'vuex';

export default {
    data () {
        return {

        }
    },

    methods: {
        onPostCreated (post) {
            const token = this.$store.getters.accessToken;
            if (post) {
                this.$store.dispatch('newPost', { post, token });
            }
        }
    },

    components: {
        PostComposer
    }
}
</script>