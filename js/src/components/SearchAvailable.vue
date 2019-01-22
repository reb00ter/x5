<template>
  <div class="search_box">
    Поиск
    <dx-select :data-source="types" valueExpr="id" displayExpr="title"/>
  </div>
</template>

<script>
import dxSelect from 'devextreme-vue/select-box'

export default {
  name: 'SearchAvailable',
  data () {
    return {}
  },
  components: {
    dxSelect
  },
  computed: {
    types () {
      return this.$store.state.types
    }
  },
  mounted () {
    this.$store.dispatch('updateContainerTypes').then(function () {
      console.log('types loaded')
    })
  }
}
</script>

<style scoped>

</style>
