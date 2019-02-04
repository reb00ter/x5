<template>
  <div class="wrapper">
    <div class="row filter_params">
      <div class="col-12">
        <h2>Настройки фильтра</h2>
        {{ filter.type_title }}, {{ filter.count }} шт.
        <span v-if="filter.date_from">с {{ filter.date_from }}</span>
        <span v-if="filter.date_till">по {{ filter.date_till }}</span>
        <div>Создано {{ filter.created }}</div>
      </div>
    </div>
    <h2>Контейнеры</h2>
    <results :results="filter.results" error="" error_text=""/>
  </div>
</template>

<script>
import Results from './results/SearchResults.vue'

export default {
  name: 'StoredFilterDetail',
  components: {
    Results
  },
  data () {
    return {
      filter: {}
    }
  }
}
</script>

<style scoped>

</style>
