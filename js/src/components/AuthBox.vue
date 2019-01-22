<template>
    <div class="user" v-if="user.email">
      {{ user.email }}
      <a href="/admin/logout/">Выйти</a>
    </div>
    <div class="user" v-else>
      <social-auth/>
    </div>
</template>

<script>
import container from '../api/containers'
import SocialAuth from './SocialAuth.vue'

export default {
  name: 'AuthBox',
  data: function () {
    return {'user': {}}
  },
  methods: {

  },
  created: function () {
    let promise = container.getCurrentUser()
    let vue = this
    promise.then(function (data) {
      console.log(data)
      vue.user = data
    })
  },
  components: {
    SocialAuth
  }
}
</script>

<style scoped>

</style>
