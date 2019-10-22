<template>
    <section class="admin-main-panel">
        <div class="is-pulled-right">
            <per-page-select v-model="perPage" />
        </div>
        <b-tabs v-model="activeTab"
            position="is-centered" class="block" expanded
        >
            <b-tab-item :label="labels.media">
                <media-table :perPage="perPage" />
            </b-tab-item>

            <b-tab-item :label="labels.avatars">
                <avatars-table :perPage="perPage" />
            </b-tab-item>
        </b-tabs>
    </section>
</template>

<script>
import PerPageSelect from '@/components/PerPageSelect.vue';
import MediaTable from '@/components/MediaTable.vue';
import AvatarsTable from '@/components/AvatarsTable.vue';

export default {
    data () {
        return {
            activeTab: 0,
            perPage: 10,

            labels: {
                media: "Uploaded media",
                avatars: "Avatars"
            }
        }
    },

    components: {
        PerPageSelect,
        MediaTable,
        AvatarsTable
    }
}
</script>

<style>

</style>