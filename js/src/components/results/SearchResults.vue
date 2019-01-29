<template>
  <div class="search_results">
    <free-container v-for="container in results" :container="container" :key="container.id"/>
    <div v-if="results.length === 0">Таких контейнеров нет</div>
    <div v-if="error" class="dx-error-message">Во время поиска произошла ошибка {{ error_text }}</div>
  </div>
</template>

<script>
import FreeContainer from './FreeContainer.vue'

export default {
  name: 'SearchResults',
  props: ['results', 'error', 'error_text'],
  components: {
    FreeContainer
  }
}
</script>

<style scoped>

</style>
