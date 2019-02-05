<template>
  <div class="col-12 col-md-6 col-lg-3">
    <div class="box">
      <div class="count">{{ container.type }} {{ container.count }} шт<span v-if="container.parts"> (можно частями)</span></div>
      <container-location :location="container.location"/>
      <div class="address">{{ container.address }}</div>
      <div class="dates">
        <span>с {{ formatDate(container.date_from) }}</span>
        <span v-if="container.date_till">по {{ formatDate(container.date_till) }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import ContainerLocation from './ContainerLocation.vue'

export default {
  name: 'FreeContainer',
  props: ['container'],
  components: {
    ContainerLocation
  },
  methods: {
    formatDate (date) {
      // YYYY-MM-DD -> DD.MM.YYYY
      return `${date.slice(8, 10)}.${date.slice(5, 7)}.${date.slice(0, 4)}`
    }
  }
}
</script>

<style scoped>
  .box{
    background-color: lightgrey;
    padding: 5px 10px;
    margin-top: 5px;
    border-radius: 5px;
    cursor: default;
  }
  .box:hover{
    background-color: orange;
  }
  .count, .dates{
    overflow-x: hidden;
    white-space: nowrap;
  }
</style>
