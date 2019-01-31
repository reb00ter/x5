<template>
  <div class="row">
    <div class="col-12">
      {{ filter_params.type_title }}, {{ filter_params.count }} шт.
      <span v-if="filter_params.date_from">с {{ filter_params.date_from }}</span>
      <span v-if="filter_params.date_till">по {{ filter_params.date_till }}</span>
      <div>Создано {{ filter_params.created }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StoredFilter',
  props: [
    'filter_params'
  ]
}
</script>

<style scoped>

</style>
