<template>
  <b-table
    :data="data"
    ref="table"
    :default-sort="['id', 'asc']"
    striped

    paginated
    backend-pagination
    :total="totalMedia"
    :per-page="perPage"
    @page-change="onPageChange"
  >
    <template v-slot="props">
        <b-table-column field="id" :label="labels.id" sortable
            width="40" numeric centered
        >
            {{ props.row.id }}
        </b-table-column>
        <b-table-column field="uri" :label="labels.uri">
            <a :href="props.row.uri" target="_blank">{{ props.row.uri }}</a>
        </b-table-column>
        <b-table-column field="uploader.username" :label="labels.uploader">
            <router-link :to="`/web/user/${props.row.uploader.id}`" target="_blank">
                {{ props.row.uploader | formatUser }}
            </router-link>
        </b-table-column>
        <b-table-column field="post.id" :label="labels.post">
            <router-link :to="`/web/post/${props.row.post.id}`" target="_blank">
                {{ props.row.post.subject | truncate(20) }}
            </router-link>
        </b-table-column>
        <b-table-column field="mimetype" :label="labels.mimetype">
                {{ props.row.mimetype }}
        </b-table-column>
        <b-table-column field="filename" :label="labels.filename">
                {{ props.row.filename }}
        </b-table-column>
    </template>
  </b-table>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data () {
        return {
            labels: {
                id: "ID",
                uri: "Location",
                uploader: "Uploader",
                post: "Post",
                filename: "Filename",
                mimetype: "Mimetype"
            }
        }
    },

    props: [
        'perPage'
    ],

    computed: {
        ...mapGetters({
            data: 'admin/media',
            totalMedia: 'admin/mediaCount',
        }),
    },

    watch: {
        perPage () {
            this.page = 1;
            this.fetchData();
        },

        mode () {
            this.fetchData();
        }
    },

    methods: {
        fetchData () {
            this.$store.dispatch('admin/getMedia', {
                max: +this.perPage,
                page: this.page,
                token: this.$store.getters.accessToken,
            });
        },

        onPageChange (page) {
            this.page = page;
            this.fetchData();
        },
    },

    filters: {
        formatUser (user) {
            return `${user.username}@${user.origin}`;
        },

        truncate (value, length) {
            return value.length > length
                    ? value.substr(0, length) + '...'
                    : value;
        }
    },

    mounted () {
        this.fetchData();
    }
}
</script>

<style>

</style>