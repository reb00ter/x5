import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api/containers'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  state: {
    mode: 'avail',
    params: {},
    results: [],
    types: [],
    locations: [],
    count: 1,
    search_error: false,
    search_error_text: ''
  },
  strict: debug,
  actions: {
    updateDictionaries (context) {
      api.getContainerTypes().then(result => context.commit('setContainerTypes', result))
      api.getLocations().then(result => context.commit('setLocations', result))
    },
    search (context, params) {
      context.commit('resetSearchError')
      context.commit('setSearchParams', params)
      if (context.state.mode === 'avail') {
        api.getFreeContainers(params).then(
          result => context.commit('setSearchResults', result),
          error => {
            context.commit('setSearchError', error)
          })
      }
    }
  },
  mutations: {
    setContainerTypes (state, types) {
      state.types = types
    },
    setLocations (state, locations) {
      state.locations = locations
    },
    setSearchParams (state, params) {
      state.params = params
    },
    setSearchResults (state, results) {
      state.results = results
    },
    setSearchError (state) {
      state.search_error = true
      state.search_error_text = ''
    },
    resetSearchError (state, e) {
      state.search_error = false
      state.search_error_text = e
    },
    showLeaf (state, leaf) {
      Vue.set(leaf, 'visible', true)
    },
    hideLeaf (state, leaf) {
      Vue.set(leaf, 'visible', false)
    },
    openLeaf (state, leaf) {
      Vue.set(leaf, 'opened', true)
    },
    closeLeaf (state, leaf) {
      Vue.set(leaf, 'opened', false)
    },
    switchLeaf (state, leaf) {
      Vue.set(leaf, 'opened', !leaf.opened)
    },
    checkLeaf (state, leaf) {
      Vue.set(leaf, 'checked', true)
    },
    uncheckLeaf (state, leaf) {
      Vue.set(leaf, 'checked', false)
    }
  }
})
