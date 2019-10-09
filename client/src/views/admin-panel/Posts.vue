<template>
    <section class="admin-main-panel">
        <div class="columns">
            <div class="column">
                <h1 class="is-title" v-if="mode == 'all'">{{ labels.allPosts }}</h1>
                <h1 class="is-title" v-else>{{ labels.localOnly }}</h1>
            </div>

            <div class="column is-narrow">
                <per-page-select v-model="perPage" />
            </div>
        </div>

        <b-table
            :data="data"
            :columns="columns"
            :default-sort="['id','asc']"
            striped
        >
        </b-table>
    </section>
</template>

<script>
import PerPageSelect from '@/components/PerPageSelect.vue';

export default {
    data () {
        return {
            perPage: 10,

            // TODO: Change to Vuex/API call/whatever
            data: [
                {
                    id: 42,
                    user: "nobody",
                    subject: "Filler",
                    content: "Nothing to see here",
                    flake: 1234567890,
                    uri: "https://example.com/posts/abc123"
                }
            ],

            labels: {
                allPosts: "All posts",
                localOnly: "Only local posts",
                columns: {
                    id: "ID",
                    user: "User",
                    subject: "Subject",
                    content: "Content",
                    flake: "Flake ID",
                    uri: "URI",
                }
            },

            columns: [],
        }
    },

    props: [
        'mode'
    ],

    methods: {
        labelFor (column) {
            return this.labels.columns[column];
        },

        /*
         * We can't access `this` in a data definition, which makes it
         * much harder to define properly localized labels for columns.
         * 
         */
        setupColumns () {
            const columns = [
                {
                    label: this.labelFor('id'),
                    field: "id",
                    width: 40,
                    numeric: true,
                    centered: true,
                    sortable: true
                },
                {
                    label: this.labelFor('user'),
                    field: "user",
                    sortable: true
                },
                {
                    label: this.labelFor('subject'),
                    field: "subject"
                },
                {
                    label: this.labelFor('content'),
                    field: "content"
                },
                {
                    label: this.labelFor('flake'),
                    field: "flake"
                },
                {
                    label: this.labelFor('uri'),
                    field: "uri"
                }
            ];

            this.columns = columns;
        }
    },

    mounted () {
        this.setupColumns();
    },

    components: {
        PerPageSelect
    }
}
</script>
