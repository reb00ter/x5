<template>
  <div class="container">
    <container-location :location="container.location"/>
    <div class="count">{{ container.count }} шт<span v-if="container.parts"> (можно частями)</span></div>
    <div class="с">{{ container.date_from }}</div>
    <div class="по" v-if="container.date_till">{{ container.date_till }}</div>
  </div>
</template>

<script>
import ContainerLocation from './ContainerLocation.vue'

export default {
  name: 'FreeContainer',
  props: ['container'],
  components: {
    ContainerLocation
  }
}
</script>

<style scoped>

</style>
