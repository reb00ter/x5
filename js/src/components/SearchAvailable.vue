<template>
  <div class="search_box">
    Поиск
    <dx-select :data-source="types" valueExpr="id" displayExpr="title" v-model="type" @change="updateType"/>
    <tree-selector :options="locations"/>
  </div>
</template>

<script>
import dxSelect from 'devextreme-vue/select-box'
import TreeSelector from './treeselector/treeselector.vue'

export default {
  name: 'SearchAvailable',
  data () {
    return {
    }
  },
  components: {
    dxSelect,
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
        return this.$store.state.type
      },
      set (value) {
        this.$store.dispatch('search', {type: value}).then(function () {
          console.log('completed')
        })
        console.log(this.$store.state.params)
      }
    }
  },
  methods: {
    updateType () {
    }
  },
  mounted () {
    this.$store.dispatch('updateDictionaries').then(function () {})
  }
}
</script>

<style scoped>

</style>
