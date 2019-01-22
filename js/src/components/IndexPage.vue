<template>
  <div class="wrapper">
    Главная страница
    <search-box/>
  </div>
</template>

<script>
import SearchBox from './SearchAvailable.vue'

export default {
  name: 'IndexPage',
  components: {
    SearchBox
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    }
  }
}
</script>

<style scoped>
</style>
