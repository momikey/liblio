import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import Buefy from 'buefy'
import i18n from './i18n'
// import 'buefy/dist/buefy.css'

Vue.config.productionTip = false

Vue.use(Buefy)

new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount('#app')
