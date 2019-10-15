<template>
    <div class="admin columns">
        <div class="column is-one-quarter side-panel">
            <b-menu>
                <b-menu-list :label="labels.menuItems.users" icon="account">
                    <b-menu-item tag="router-link" to="/admin/users/local"
                        :label="labels.menuItems.localUsers"
                    >

                    </b-menu-item>
                    <b-menu-item tag="router-link" to="/admin/users/all"
                        :label="labels.menuItems.allUsers"
                    >

                    </b-menu-item>
                </b-menu-list>                

                <b-menu-list :label="labels.menuItems.posts" icon="post">
                    <b-menu-item tag="router-link" to="/admin/posts/local"
                        :label="labels.menuItems.localPosts"
                    >

                    </b-menu-item>
                    <b-menu-item tag="router-link" to="/admin/posts/all"
                        :label="labels.menuItems.allPosts"
                    >

                    </b-menu-item>
                </b-menu-list>

                <b-menu-list :label="labels.menuItems.tags" icon="tag">
                    <b-menu-item tag="router-link" to="/admin/tags"
                        :label="labels.menuItems.tags"
                    >

                    </b-menu-item>
                </b-menu-list>

                <b-menu-list :label="labels.menuItems.other" icon="settings">
                    <b-menu-item tag="router-link" to="/admin/uploads"
                        :label="labels.menuItems.uploads"
                    >

                    </b-menu-item>

                    <b-menu-item tag="router-link" to="/admin/settings"
                        :label="labels.menuItems.settings"
                    >

                    </b-menu-item>
                    <b-menu-item tag="router-link" to="/web"
                        icon="logout" :label="labels.menuItems.exit"
                    >
                    </b-menu-item>
                </b-menu-list>
            </b-menu>
        </div>
        <div class="column is-three-quarters">
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            labels: {
                menuItems: {
                    users: "Users",
                    localUsers: "Local users",
                    allUsers: "All users",

                    posts: "Posts",
                    localPosts: "Local posts",
                    allPosts: "All posts",

                    tags: "Tags",

                    other: "Other actions",

                    uploads: "Uploads",
                    
                    settings: "Site settings",
                    exit: "Exit"
                }
            }
        }
    }
}
</script>

<style scoped>
    .column.side-panel {
        min-height: calc(100vh - 108px);
        overflow-y: auto;
    }

    .menu-label .icon {
        padding-right: 8px;
    }
</style>
