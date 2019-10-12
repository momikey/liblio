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
            ref="table"
            :default-sort="['id','asc']"
            striped

            detailed
            :show-detail-icon="false"
            detail-key="id"

            paginated
            backend-pagination
            :total="totalPosts"
            :per-page="perPage"
            @page-change="onPageChange"
        >
            <template slot-scope="props">
                <b-table-column field="id" :label="labels.columns.id" sortable
                    width="40" numeric centered
                >
                    <span @click="toggleRow(props.row)">
                        {{ props.row.id }}
                    </span>
                </b-table-column>

                <b-table-column field="user" :label="labels.columns.user" sortable>
                    <span @click="toggleRow(props.row)">
                        {{ props.row.user | formatUser }}
                    </span>
                </b-table-column>

                <b-table-column field="subject" :label="labels.columns.subject">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.subject | truncate(16) }}
                    </span>
                </b-table-column>

                <b-table-column field="content" :label="labels.columns.content">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.content | truncate(16) }}
                    </span>
                </b-table-column>

                <b-table-column field="flake" :label="labels.columns.flake">
                    {{ props.row.flake }}
                </b-table-column>

                <b-table-column field="uri" :label="labels.columns.uri">
                    {{ props.row.uri }}
                </b-table-column>
            </template>

            <template slot="detail" slot-scope="props">
                <article>
                    <h1 class="is-title is-size-5 has-text-weight-bold">{{ props.row.subject }}</h1>
                    <p>
                        {{ props.row.content }}
                    </p>
                </article>
            </template>
        </b-table>
    </section>
</template>

<script>
import PerPageSelect from '@/components/PerPageSelect.vue';
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            perPage: 10,
            page: 1,

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

    computed: {
        ...mapGetters({
            data: 'admin/posts',
            totalPosts: 'admin/postCount',
        })
    },

    props: [
        'mode'
    ],

    methods: {
        labelFor (column) {
            return this.labels.columns[column];
        },

        fetchData () {
            this.$store.dispatch('admin/getPosts', {
                max: +this.perPage,
                page: this.page,
                token: this.$store.getters.accessToken
            });
        },

        toggleRow (row) {
            this.$refs.table.toggleDetails(row);
        },

        onPageChange (page) {
            this.page = page;
            this.fetchData();
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
                    field: "user.display_name",
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

    watch: {
        perPage () {
            this.page = 1;
            this.fetchData();
        }
    },

    mounted () {
        this.setupColumns();
        this.fetchData();
    },

    components: {
        PerPageSelect
    }
}
</script>
