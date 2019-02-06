<template>
  <div class="search_box">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-4 search_box__inner">
          <div class="row">
            <div class="title-search">
              <p>Поиск контейнеров</p>
            </div>
            <div class="search_box__item col-12">
              <input type="radio" name="mode" value="avail" id="avail" v-model="mode">
              <label for="avail">Я ищу</label>
              <input type="radio" name="mode" value="need" id="need" v-model="mode">
              <label for="need">У меня есть</label>
            </div>
            <div class="search_box__item col-md-4 col-xs-6">
              <label>Количество</label>
              <dx-num v-model="count" :min="1"/>
            </div>
            <div class="search_box__item col-md-8 col-xs-6">
              <label>Тип</label>
              <dx-select :data-source="types" valueExpr="id" displayExpr="title" v-model="type"/>
            </div>
            <div class="search_box__item col-md-6 col-xs-12">
              <label>С</label>
              <dx-date v-model="date_from" style="width: 100%"/>
            </div>
            <div class="search_box__item col-md-6 col-xs-12">
              <label>По</label>
              <dx-date v-model="date_till" :min="param_date_from" style="width: 100%"/>
            </div>
            <div class="search_box__item col-12">
              <label>Расположение</label>
              <tree-selector :options="locations" @change="updateLocations"/>
            </div>
          </div>
          <div class="row" v-if="auth_done">
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
  props: ['auth_done'],
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
    },
    mode: {
      get () {
        return this.$store.state.mode
      },
      set (value) {
        this.$store.commit('setMode', value)
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
      switch (this.$store.state.mode) {
        case 'avail':
          api.storeFreeSearchParams({
            count: this.param_count,
            type: this.param_type,
            date_from: this.param_date_from,
            date_till: this.param_date_till,
            location: this.param_location,
            location_city: this.param_location__city,
            location_city_region: this.param_location__city__region
          })
          break
        case 'need':
          api.storeNeedSearchParams({
            count: this.param_count,
            type: this.param_type,
            date_from: this.param_date_from,
            date_till: this.param_date_till,
            location: this.param_location,
            location_city: this.param_location__city,
            location_city_region: this.param_location__city__region
          })
          break
      }
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
  .search_box{
    background-image: url("../assets/containers.jpg");
    background-size: cover;
  }
  .search_box__inner{
    padding: 15px;
    margin: 20px 0;
    background-color: rgba(255, 255, 255, 0.75);
    border: 1px solid #e3e3e3;
    -moz-box-shadow: 0 13px 16px rgba(0, 0, 0, 0.5);
    -webkit-box-shadow: 0 13px 16px rgba(0, 0, 0, 0.5);
    box-shadow: 0 13px 16px rgba(0, 0, 0, 0.5);
  }
  .title-search {
    text-align: center;
    margin-top: 2px;
    height: 45px;
    width: 100%;
  }
  .title-search p {
    color: #f88e1d;
    font-size: 14px;
    padding-top: 12px;
    font-weight: bold;
    text-transform: uppercase;
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
