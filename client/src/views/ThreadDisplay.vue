<template>
    <section class="thread-display">
        <template v-if="threadParent">
            <post-thread
                :parent="threadParent"
                :children="threadChildren"
            />
        </template>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

import PostThread from '@/components/PostThread.vue'

export default {
    data () {
        return {

        }
    },

    props: [
        'postid'
    ],

    computed: {
        ...mapGetters(['thread', 'threadParent', 'threadChildren'])
    },

    methods: {
        fetch (id) {
            this.$store.dispatch('getThread', id);
        }
    },

    created () {
        this.fetch(this.postid);
    },

    beforeRouteUpdate(to, from, next) {
        this.fetch(to.params.postid);
        next();
    },

    components: {
        PostThread
    }
}
</script>