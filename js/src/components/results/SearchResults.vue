<template>
  <div class="search_results">
    <free-container v-for="container in results" :container="container" :key="container.id"/>
  </div>
</template>

<script>
import FreeContainer from './FreeContainer.vue'

export default {
  name: 'SearchResults',
  props: ['results'],
  components: {
    FreeContainer
  }
}
</script>

<style scoped>

</style>
