<template>
  <div class="wrapper">
    <stored-filter v-for="filter in free_items" :filter_params="filter" :key="filter.id"/>
  </div>
</template>

<script>
import api from '../api/containers'
import StoredFilter from './StoredFilter.vue'

export default {
  name: 'StoredFilters',
  components: {
    StoredFilter
  },
  data () {
    return {
      free_items: []
    }
  },
  created: function () {
    let app = this
    api.getMyFreeSearchParams().then(function (data) {
      app.free_items = data
    })
  }
}
</script>

<style scoped>

</style>
