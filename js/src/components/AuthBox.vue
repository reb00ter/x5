<template>
    <div class="user" v-if="user.email">
      {{ user.email }}
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
