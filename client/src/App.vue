<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/directory">Users</router-link> |
      <router-link to="/new-account">New Account</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

/* custom styles go here */

@import "~bulma";
@import "~buefy/src/scss/buefy";

.has-text-primary-inverted {
  color: findColorInvert($primary);
}

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
</style>
