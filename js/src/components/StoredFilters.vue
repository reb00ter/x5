<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 col-md-4">
        <h2 v-if="free_items.length > 0">Свободные контейнеры</h2>
        <stored-filter v-for="filter in free_items" :filter_params="filter" :key="'free' + filter.id" @click.native="setActiveFree(filter)"
                       :class="{selected: (filter.id===active)&&(active_type==='free')}"/>
        <h2 v-if="need_items.length > 0">Искомые контейнеры</h2>
        <stored-filter v-for="filter in need_items" :filter_params="filter" :key="'need' + filter.id" @click.native="setActiveNeed(filter)"
                       :class="{selected: (filter.id===active)&&(active_type==='need')}"/>
        <div v-if="(free_items.length+need_items.length) === 0">
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
      need_items: [],
      active: null,
      active_type: '',
      active_data: null
    }
  },
  created: function () {
    let app = this
    api.getMyFreeSearchParams().then(function (data) {
      app.free_items = data
    })
    api.getMyNeedSearchParams().then(function (data) {
      app.need_items = data
    })
  },
  methods: {
    setActiveFree (item) {
      this.active = item.id
      this.active_type = 'free'
      let vue = this
      api.getStoredFreeSearchParamsResults(item.id).then(function (data) {
        vue.active_data = data
      })
    },
    setActiveNeed (item) {
      this.active = item.id
      this.active_type = 'need'
      let vue = this
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
