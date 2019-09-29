<template>
    <div class="level tag-list">
        <div :class="alignmentClass">
            <b-tag rounded class="level-item"
                v-for="tag in tags" :key="tag.key"
            >
                <router-link :to="`web/${uriForTag(tag.key)}`">{{ tag.value }}</router-link>
            </b-tag>
        </div>
    </div>
</template>

<script>
import { uriForTag } from "@/modules/uri";

export default {
    data () {
        return {

        }
    },

    props: [
        'tags',
        'align'
    ],

    computed: {
        alignmentClass () {
            switch (this.align) {
                case 'left':
                    return 'level-left';
                case 'right':
                    return 'level-right';
                default:
                    return 'level-item';
            }
        }
    },

    methods: {
        uriForTag
    }
}
</script>

<style>
    .tag-list .tag {
        margin-left: 0.25rem;
        margin-right: 0.25rem;
    }
</style>
