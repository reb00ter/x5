<template>
    <div class="user" v-if="user.id">
      {{ user.username }}
      <a href="/accounts/logout/">Выйти</a>
    </div>
    <div class="user" v-else>
      <a href="/accounts/login">Авторизоваться</a>
    </div>
</template>

<script>

export default {
  name: 'AuthBox',
  data: function () {
  },
  props: [
    'user'
  ],
  methods: {

  },
  components: {
  }
}
</script>

<style scoped>

</style>
