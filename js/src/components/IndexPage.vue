<template>
  <div class="wrapper">
    <search-box :auth_done="user.id !== null"/>
    <results :results="results" :error="error" :error_text="error_text"/>
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
  },
  computed: {
    user () {
      return this.$store.state.user
    },
    results () {
      return this.$store.state.results
    },
    error () {
      return this.$store.state.search_error
    },
    error_text () {
      return this.$store.state.search_error_text
    }
  }
}
</script>

<style scoped>
</style>
