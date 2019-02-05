<template>
  <div id="app">
    <div class="page">
      <div class="page-header">
        <div class="container">
          <b-navbar toggleable="lg" type="light">
            <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
            <b-navbar-brand href="#">Контейнеры</b-navbar-brand>
            <b-collapse is-nav id="nav_collapse">
              <main-menu :auth_done="user.id !== null"/>
            </b-collapse>
            <auth-box :user="user"/>
          </b-navbar>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import api from './api/containers'
import AuthBox from './components/AuthBox.vue'
import MainMenu from './components/MainMenu.vue'
import DxButton from 'devextreme-vue/button'
import bNavbar from 'bootstrap-vue/es/components/navbar/navbar'
import bCollapse from 'bootstrap-vue/es/components/collapse/collapse'
import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand'
import bNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav'
import bNavbarToggle from 'bootstrap-vue/es/components/navbar/navbar-toggle'

export default {
  name: 'App',
  components: {
    bNavbar,
    bCollapse,
    bNavbarBrand,
    bNavbarNav,
    bNavbarToggle,
    DxButton,
    MainMenu,
    AuthBox
  },
  data () {
    return {}
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    }
  },
  computed: {
    user () {
      return this.$store.state.user
    }
  },
  created: function () {
    let app = this
    api.getCurrentUser().then(function (data) {
      app.$store.commit('setUser', data)
    })
  }
}
</script>

<style>
.logo{
  background-image: url("./assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
}
.auth{
  float: right;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
