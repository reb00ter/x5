<template>
  <div class="search_box">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-4 search_box__inner">
          <div class="row">
            <div class="search_box__item col-12">
              <label>Расположение</label>
              <tree-selector :options="locations" @change="updateLocations"/>
            </div>
            <div class="search_box__item col-12">
              <label>Тип</label>
              <dx-select :data-source="types" valueExpr="id" displayExpr="title" v-model="type"/>
            </div>
            <div class="search_box__item col-4">
              <label>Количество</label>
              <dx-num v-model="count" min="1"/>
            </div>
            <div class="search_box__item col-4">
              <label>С</label>
              <dx-date v-model="date_from"/>
            </div>
            <div class="search_box__item col-4">
              <label>По</label>
              <dx-date v-model="date_till" :min="param_date_from"/>
            </div>
          </div>
          <div class="row">
            <div class="store_button_container col-12">
              <dx-button text="Сохранить поиск" @click="store"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api/containers'
import dxSelect from 'devextreme-vue/select-box'
import dxButton from 'devextreme-vue/button'
import dxNum from 'devextreme-vue/number-box'
import dxDate from 'devextreme-vue/date-box'
import TreeSelector from './treeselector/treeselector.vue'

export default {
  name: 'SearchAvailable',
  data () {
    return {
      param_count: 1,
      param_type: null,
      param_date_from: null,
      param_date_till: null,
      param_location: [],
      param_location__city: [],
      param_location__city__region: []
    }
  },
  components: {
    dxButton,
    dxSelect,
    dxNum,
    dxDate,
    TreeSelector
  },
  computed: {
    types () {
      return this.$store.state.types
    },
    locations () {
      return this.$store.state.locations
    },
    type: {
      get () {
        return this.$store.state.params.type
      },
      set (value) {
        this.param_type = value
        this.search()
      }
    },
    count: {
      get () {
        return this.$store.state.params.count
      },
      set (value) {
        this.param_count = value
        this.search()
      }
    },
    date_from: {
      get () {
        return this.$store.state.params.date_from
      },
      set (value) {
        this.param_date_from = value
        this.search()
      }
    },
    date_till: {
      get () {
        return this.$store.state.params.date_till
      },
      set (value) {
        this.param_date_till = value
        this.search()
      }
    }
  },
  methods: {
    search () {
      this.$store.dispatch('search', {
        count: this.param_count,
        type: this.param_type,
        date_from: this.param_date_from,
        date_till: this.param_date_till,
        location: this.param_location,
        location__city: this.param_location__city,
        location__city__region: this.param_location__city__region
      }).catch(function () {

      })
    },
    store () {
      api.storeFreeSearchParams({
        count: this.param_count,
        type: this.param_type,
        date_from: this.param_date_from,
        date_till: this.param_date_till,
        location: this.param_location,
        location_city: this.param_location__city,
        location_city_region: this.param_location__city__region
      })
    },
    updateLocations (data) {
      this.param_location = []
      this.param_location__city = []
      this.param_location__city__region = []
      let app = this
      data.forEach(function (elem) {
        switch (elem.type) {
          case 'location':
            app.param_location.push(elem.id)
            break
          case 'location__city':
            app.param_location__city.push(elem.id)
            break
          case 'location__city__region':
            app.param_location__city__region.push(elem.id)
            break
        }
      })
      this.search()
    }
  },
  mounted () {
    this.$store.dispatch('updateDictionaries').then(function () {})
  }
}
</script>

<style scoped>
  .search_box__inner{
    background-color: lightgray;
    padding: 15px;
  }
  label{
    margin-bottom: 0;
    margin-top: .5rem;
  }
</style>
<style>
  .dx-datebox.dx-auto-width.dx-dropdowneditor-button-visible
  .dx-texteditor-input,
  .dx-datebox:not(.dx-texteditor-empty)
  .dx-auto-width.dx-dropdowneditor-button-visible
  .dx-texteditor-input {
    padding-right: 22px;
  }
</style>
