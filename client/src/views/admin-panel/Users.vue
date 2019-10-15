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
            :total="totalUsers"
            :per-page="perPage"
            @page-change="onPageChange"
        >
            <template v-slot="props" v-if="mode === 'all'">
                <b-table-column field="id" :label="labels.columns.all.id" sortable
                    width="40" numeric centered
                >
                    <span @click="toggleRow(props.row)">
                        {{ props.row.id }}
                    </span>
                </b-table-column>

                <b-table-column field="display_name" :label="labels.columns.all.displayName">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.display_name }}
                    </span>
                </b-table-column>

                <b-table-column field="username" :label="labels.columns.all.username" sortable>
                    <span @click="toggleRow(props.row)">
                        {{ props.row.username }}
                    </span>
                </b-table-column>

                <b-table-column field="origin" :label="labels.columns.all.origin" sortable>
                    <span @click="toggleRow(props.row)">
                        {{ props.row.origin }}
                    </span>
                </b-table-column>

                <b-table-column field="private" :label="labels.columns.all.private">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.private }}
                    </span>
                </b-table-column>
            </template>

            <template v-slot="props" v-else>
                <b-table-column field="id" :label="labels.columns.local.id" sortable
                    width="40" numeric centered
                >
                    <span @click="toggleRow(props.row)">
                        {{ props.row.id }}
                    </span>
                </b-table-column>
                
                <b-table-column field="username" :label="labels.columns.local.username" sortable>
                    <span @click="toggleRow(props.row)">
                        {{ props.row.username }}
                    </span>
                </b-table-column>

                <b-table-column field="email" :label="labels.columns.local.email">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.email }}
                    </span>
                </b-table-column>

                <b-table-column field="userdata.display_name" :label="labels.columns.local.displayName">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.userdata && props.row.userdata.display_name }}
                    </span>
                </b-table-column>

                <b-table-column field="userdata.private" :label="labels.columns.local.private">
                    <span @click="toggleRow(props.row)">
                        {{ props.row.userdata && props.row.userdata.private }}
                    </span>
                </b-table-column>
            </template>

            <template #detail="props">
                <article class="columns" v-if="mode === 'all'">
                    <div class="column is-three-quarters">
                        <p>
                            {{ props.row.bio }}
                        </p>
                        <!-- TODO: User detail, which should switch based on mode -->
                    </div>
                    <div class="column is-one-quarter">

                    </div>
                </article>
                <article class="columns" v-else>
                    <div class="column is-three-quarters">

                    </div>
                    <div class="column is-one-quarter">
                        <b-menu class="admin-panel-actions">
                            <!-- TODO: Add menu items (global mute, password reset, etc.) -->
                            <b-menu-list>
                                <b-menu-item
                                    :label="labels.menu.passwordReset"
                                />
                                <b-menu-item
                                    :label="labels.menu.suspendUser"
                                />
                                <b-menu-item
                                    :label="labels.menu.banUser"
                                />
                            </b-menu-list>
                        </b-menu>
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
                users: "All users",
                accounts: "Local accounts",
                columns: {
                    local: {
                        id: "ID",
                        username: "Username",
                        displayName: "Display name",
                        email: "Email",
                        lastLogin: "Last login",
                        lastAction: "Last action",
                        role: "Role",
                        private: "Private"
                    },

                    all: {
                        id: "ID",
                        username: "Username",
                        origin: "Origin",
                        displayName: "Display name",
                        private: "Private"
                    }
                },

                menu: {
                    passwordReset: "Reset password",
                    suspendUser: "Suspend user",
                    banUser: "Ban user"
                }
            }
        }
    },

    computed: {
        ...mapGetters({
            data: 'admin/users',
            totalUsers: 'admin/userCount',
        }),

        origin () {
            return this._mode === 'local' ? this.$store.getters.host : undefined;
        }
    },

    props: [
        'mode'
    ],

    methods: {
        fetchData () {
            this.$store.dispatch('admin/getUsers', {
                max: +this.perPage,
                page: this.page,
                token: this.$store.getters.accessToken,
                origin: this.mode === 'local' ? this.$store.getters.host : undefined,
                mode: this.mode
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
        this.fetchData();
    },

    components: {
        PerPageSelect
    }
}
</script>