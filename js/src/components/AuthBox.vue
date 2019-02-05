<template>
  <div class="navbar-right">
    <div class="user" v-if="user.id">
      {{ user.username }}
      <a href="/accounts/logout/">Выйти</a>
    </div>
    <div class="user" v-else>
      <a href="#" @click="showModal">Авторизоваться</a>
    </div>
    <b-modal ref="AuthModal" hide-footer title="Авторизация">
      <div v-html="auth_form"/>
      <b-btn block @click="hideModal">Отмена</b-btn>
    </b-modal>
  </div>
</template>

<script>
import bModal from 'bootstrap-vue/es/components/modal/modal'
import bBtn from 'bootstrap-vue/es/components/button/button'
import api from '../api/containers'

export default {
  name: 'AuthBox',
  data: function () {
    return {
      auth_form: ''
    }
  },
  props: [
    'user'
  ],
  methods: {
    showModal () {
      let vue = this
      api.getAuthDlg().then(function (data) {
        vue.auth_form = data
      }).catch(function (data) {
      })
      this.$refs.AuthModal.show()
    },
    hideModal () {
      this.$refs.AuthModal.hide()
    }
  },
  components: {
    bModal,
    bBtn
  }
}
</script>

<style scoped>

</style>
