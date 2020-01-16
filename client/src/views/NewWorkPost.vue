<template>
    <work-composer class="work-composer"
        @post-created="onWorkPostCreated"
    />
</template>

<script>
import WorkComposer from "@/components/WorkComposer.vue";
import { mapActions } from 'vuex';

export default {
    data () {
        return {

        }
    },

    methods: {
        onWorkPostCreated (post) {
            const token = this.$store.getters.accessToken;
            if (post) {
                this.$store.dispatch('newWorkPost', { post, token });
            }
        }
    },

    components: {
        WorkComposer
    }
}
</script>