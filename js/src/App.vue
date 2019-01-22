<template>
  <div id="app">
    <div class="page">
      <div class="page-header">
        <div class="container-fluid">
          <div class="row">
            <div class="logo col-sm-2"></div>
            <div class="title col-sm-8">Контейнеры</div>
            <div class="auth col-sm-2"><auth-box/></div>
          </div>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import AuthBox from './components/AuthBox.vue'
import DxButton from 'devextreme-vue/button'
export default {
  name: 'App',
  components: {
    DxButton,
    AuthBox
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    }
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
