<template>
    <div class="user" v-if="user.email">
      <router-link :to="{ name: 'index' }">Главная</router-link>
      <router-link :to="{ name: 'StoredFilters' }">Сохранённые фильтры</router-link>
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
    let app = this
    container.getCurrentUser().then(function (data) {
      app.user = data
    })
  },
  components: {
    SocialAuth
  }
}
</script>

<style scoped>

</style>
