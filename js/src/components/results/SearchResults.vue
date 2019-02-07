<template>
  <div class="search_results">
    <div class="container">
      <!--<div class="row">-->
        <!--<container-pack v-for="container in results" :container="container" :key="container.id" @click.native="$emit('select', container)"/>-->
        <!--<div v-if="results.length === 0">Таких контейнеров нет</div>-->
        <!--<div v-if="error" class="dx-error-message">Во время поиска произошла ошибка {{ error_text }}</div>-->
      <!--</div>-->
      <div class="row">
        <dx-data-grid :dataSource="results" :masterDetail="masterDetail" :columns="columns"
                      :allowColumnResizing="true" columnResizingMode="widget"/>
      </div>
    </div>
  </div>
</template>

<script>
import ContainerPack from './ContainerPack.vue'
import dxDataGrid from 'devextreme-vue/data-grid'

export default {
  name: 'SearchResults',
  props: ['results', 'error', 'error_text'],
  components: {
    ContainerPack,
    dxDataGrid
  },
  methods: {
  },
  data () {
    return {
      masterDetail: {
        enabled: true,
        template: function (container, info) {
          if (info.data.contact) {
            container.innerHTML = `<p>Контактная ифнормация: ${info.data.contact.username} ${info.data.contact.last_name} ${info.data.contact.first_name}</p>`
            if (info.data.email) {
              container.innerHTML += `<p>Email: ${info.data.email}</p>`
            }
          }
        }
      },
      columns: [
        {
          dataField: 'type_title',
          caption: 'Тип',
          allowResizing: true
        },
        { dataField: 'count', caption: 'Количество' },
        { dataField: 'parts', caption: 'Можно частями' },
        {
          caption: 'Расположение',
          calculateCellValue: function (rowData) {
            return `${rowData.location_data.title}, ${rowData.location_data.city.title}, ${rowData.location_data.city.region}`
          },
          allowResizing: true
        },
        {
          dataField: 'address',
          caption: 'Адрес',
          allowResizing: true
        },
        { dataField: 'date_from', caption: 'С' },
        { dataField: 'date_till', caption: 'По' }
      ]
    }
  }
}
</script>

<style scoped>

</style>
