<template>
    <section class="admin-main-panel">
        <div class="columns">
            <div class="column">
                <h1 class="is-title">{{ labels.title }}</h1>
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
            :total="totalTags"
            :per-page="perPage"
            @page-change="onPageChange"
        >
            <template v-slot="props">
                <b-table-column field="id" :label="labels.columns.id" sortable
                    width="40" numeric centered
                >
                    <span @click="toggleRow(props.row)">
                        {{ props.row.id }}
                    </span>
                </b-table-column>

                <b-table-column field="name" :label="labels.columns.name" sortable>
                    <span @click="toggleRow(props.row)">
                        {{ props.row.name }}
                    </span>
                </b-table-column>
                
                <b-table-column field="description" :label="labels.columns.description">
                    <span>
                        {{ props.row.description }}
                    </span>
                </b-table-column>
            </template>

            <template #detail="props">
                <article class="columns">
                    <div class="column is-three-quarters">
                        <!-- TODO: Tag editor -->
                    </div>
                    <div class="column is-one-quarter">
                        <!-- TODO: Add actions -->
                    </div>
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
                title: "Tags",

                columns: {
                    id: "ID",
                    name: "Name",
                    description: "Description"
                }
            }
        }
    },

    computed: {
        ...mapGetters({
            data: 'admin/tags',
            totalTags: 'admin/tagCount',
        }),
    },

    methods: {
        fetchData () {
            this.$store.dispatch('admin/getTags', {
                max: +this.perPage,
                page: this.page,
                token: this.$store.getters.accessToken,
            });
        },

        toggleRow (row) {
            this.$refs.table.toggleDetails(row);
        },

        onPageChange (page) {
            this.page = page;
            this.fetchData();
        },
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

    mounted () {
        this._mode = this.mode;
        this.fetchData();
    },

    components: {
        PerPageSelect
    }
}
</script>

<style>

</style>