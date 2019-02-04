<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 col-md-4">
        <stored-filter v-for="filter in free_items" :filter_params="filter" :key="filter.id" @click.native="setActive(filter)"
                       :class="{selected: filter.id===active}"/>
        <div v-if="free_items.length === 0">
          Сохранённые наборы фильтров не найдены
        </div>
      </div>
      <div class="col-12 col-md-8" v-if="active_data !== null">
        <results :results="active_data" error="" error_text=""/>
      </div>
      <div class="col-12 col-md-8" v-else>
        Выберите один из сохранённых фильтров
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api/containers'
import StoredFilter from './StoredFilterItem.vue'
import Results from './results/SearchResults.vue'

export default {
  name: 'StoredFilters',
  components: {
    StoredFilter,
    Results
  },
  data () {
    return {
      free_items: [],
      active: null,
      active_data: null
    }
  },
  created: function () {
    let app = this
    api.getMyFreeSearchParams().then(function (data) {
      app.free_items = data
    })
  },
  methods: {
    setActive (item) {
      this.active = item.id
      let vue = this
      console.log('active changed')
      api.getStoredFreeSearchParamsResults(item.id).then(function (data) {
        vue.active_data = data
      })
    }
  }
}
</script>

<style scoped>
.selected{
  background-color: orange;
}
</style>
