import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App.vue'
import store from './store'
import router from './router'
import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'

Vue.config.productionTip = false

Vue.use(Buefy)
Vue.use(VueResource)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
