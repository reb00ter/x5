<template>
  <div class="wrapper">
    <search-box :auth_done="user.id !== null"/>
    <results :results="results" :error="error" :error_text="error_text" @select="openModal"/>
    <b-modal hide-footer title="Данные о партии контейнеров" v-model="showDetail" v-if="selected !== null">
      {{selected}}
    </b-modal>
  </div>
</template>

<script>
import SearchBox from './SearchAvailable.vue'
import Results from './results/SearchResults.vue'
import bModal from 'bootstrap-vue/es/components/modal/modal'

export default {
  name: 'IndexPage',
  components: {
    SearchBox,
    Results,
    bModal
  },
  methods: {
    openModal: function (elem) {
      this.selected = elem
      this.showDetail = true
    }
  },
  data () {
    return {
      selected: null,
      showDetail: false
    }
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
