<template>
  <div class="search_box">
    Поиск
    <dx-select :data-source="types" valueExpr="id" displayExpr="title" v-model="type" @change="updateType"/>
  </div>
</template>

<script>
import dxSelect from 'devextreme-vue/select-box'

export default {
  name: 'SearchAvailable',
  data () {
    return {
    }
  },
  components: {
    dxSelect
  },
  computed: {
    types () {
      return this.$store.state.types
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
    this.$store.dispatch('updateContainerTypes').then(function () {})
  }
}
</script>

<style scoped>

</style>
