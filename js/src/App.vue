<template>
  <div id="app">
    <div class="page">
      <div class="page-header">
        <div class="container-fluid">
          <div class="row">
            <div class="title col-sm-2">Контейнеры</div>
            <div class="menu col-sm-8"><main-menu :auth_done="user.id !== null"/></div>
            <div class="auth col-sm-2"><auth-box :user="user"/></div>
          </div>
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

export default {
  name: 'App',
  components: {
    DxButton,
    MainMenu,
    AuthBox
  },
  data () {
    return {
      user: {
        email: ''
      }
    }
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    }
  },
  created: function () {
    let app = this
    api.getCurrentUser().then(function (data) {
      console.log(data)
      app.user = data
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
  text-align: center;
  color: #2c3e50;
}
</style>
