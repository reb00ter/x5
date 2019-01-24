<template>
  <div class="wrapper">
    Главная страница
    <search-box/>
    <results :results="results"/>
  </div>
</template>

<script>
import SearchBox from './SearchAvailable.vue'
import Results from './results/SearchResults.vue'

export default {
  name: 'IndexPage',
  components: {
    SearchBox,
    Results
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    }
  },
  computed: {
    results () {
      return this.$store.state.results
    }
  }
}
</script>

<style scoped>
</style>
