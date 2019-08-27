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
        }
    }
</script>


<style lang="scss">
@import "~bulma/sass/utilities/_all";

/* custom styles go here */
$mdi-font-path: "~@mdi/font/fonts";
@import "~@mdi/font/scss/materialdesignicons";

@import "~bulma";
@import "~bulma-badge/src/sass/index.sass";
@import "~buefy/src/scss/buefy";

.has-text-primary-inverted {
    color: findColorInvert($primary);
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
}

.side-panel {
    background-color: #ffeedd;
    height: 100%;
    padding-top: 32px;
}
</style>
