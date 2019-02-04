<template>
  <div class="filter-item">
    <!--<router-link :to="{ name: 'StoredFilterDetail', params: { id: filter_params.id } }">{{ filter_params.type_title }}, {{ filter_params.count }} шт.</router-link>-->
    {{ filter_params.type_title }}, {{ filter_params.count }} шт.
    <span v-if="filter_params.date_from">с {{ filter_params.date_from }}</span>
    <span v-if="filter_params.date_till">по {{ filter_params.date_till }}</span>
    <div>Создано {{ filter_params.created }}</div>
  </div>
</template>

<script>
export default {
  name: 'StoredFilterItem',
  props: [
    'filter_params'
  ]
}
</script>

<style scoped>

</style>
