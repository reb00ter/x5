// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ruMessages from 'devextreme/localization/messages/ru.json'
import 'bootstrap/dist/css/bootstrap.css'
import 'devextreme/dist/css/dx.common.css'
import 'devextreme/dist/css/dx.light.compact.css'
import { locale, loadMessages } from 'devextreme/localization'

loadMessages(ruMessages)
locale(navigator.language || navigator.browserLanguage)

Vue.config.productionTip = false
Vue.config.devtools = true

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
