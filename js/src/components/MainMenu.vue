<template>
  <ul class="nav">
    <li class="nav-item"><router-link class="nav-link" :to="{ name: 'index' }">Главная</router-link></li>
    <li class="nav-item" v-if="auth_done"><router-link class="nav-link" :to="{ name: 'StoredFilters' }">Сохранённые фильтры</router-link></li>
  </ul>
</template>

<script>
export default {
  name: 'MainMenu',
  props: ['auth_done']
}
</script>

<style scoped>

</style>
