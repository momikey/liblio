<template>
    <div id="app">
        <navigation-bar />

        <router-view />
    </div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue";

export default {
    components: {
        NavigationBar
    },

    mounted () {
        if (this.$store.getters.user && this.$store.getters.accessToken) {
            this.$store.dispatch('initiateRefresh');
        }
    }
}
</script>


<style lang="scss">
@import "~bulma/sass/utilities/_all";

/* custom styles go here */
$mdi-font-path: "~@mdi/font/fonts";

$liked-icon: $yellow;
$shared-icon: $primary;

/* Custom colors */
$addColors: (
    "liked-icon": ($liked-icon, findColorInvert($liked-icon)),
    "shared-icon": ($shared-icon, findColorInvert($shared-icon))
);

$colors: map-merge($colors, $addColors);

@import "~@mdi/font/scss/materialdesignicons";

@import "~bulma";
@import "~bulma-badge/src/sass/index.sass";
@import "~buefy/src/scss/buefy";

.has-text-primary-inverted {
    color: findColorInvert($primary);
}

/* Use this to clear link color from <a> elements */
.has-text-main {
    color: $text;
}

/* Side panel background color */
$side-panel: #ffeedd;

#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

#nav {
    padding: 30px;

    a {
        font-weight: bold;
        color: #2c3e50;
        &.router-link-exact-active {
            color: #42b983;
        }
    }
}

.columns {
    padding-left: 24px;
    padding-right: 24px;
    max-height: 100vh;
}

.column.is-two-thirds {
    max-height: calc(100vh - 108px);
    overflow-y: auto;
}

.column.is-one-third {
    max-height: calc(100vh - 100px);
}

.side-panel {
    background-color: #ffeedd;
    padding-top: 32px;
    overflow: auto;
}

.parent-link {
    color: $text;
}

.parent-link:hover {
    color: $primary;
}

.post-metadata {
    display: inline-flex;
    align-items: center;
}

.post-metadata span {
    flex-shrink: 1;
    padding: 0;
}

.post-metadata span a {
    padding-left: 0.25rem;
}

.post-image-container {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    margin: 8px 1rem;
}

.post-image-container > * {
    padding-left: 8px;
    padding-right: 8px;
}

.admin-panel-actions a {
    color: $info;
}

.thumbnail {
    max-width: 100%;
    max-height: 100%;
}

// .is-liked-icon {
//     color: $liked-icon;
// }

// .is-shared-icon {
//     color: $shared-icon;
// }
</style>
