<template>
  <div class="location">
    {{ location.title }}, {{ location.city.title }}, {{ location.city.region }}
  </div>
</template>

<script>
export default {
  name: 'ContainerLocation',
  props: ['location']
}
</script>

<style scoped>
  .location{
    overflow-x: hidden;
    white-space: nowrap;
  }
</style>
