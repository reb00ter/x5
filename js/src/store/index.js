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
    types: []
  },
  strict: debug,
  actions: {
    updateContainerTypes (context) {
      api.getContainerTypes().then(result => context.commit('setContainerTypes', result))
    },
    search (context, params) {
      context.commit('setSearchParams', params)
      if (context.state.mode === 'avail') {
        api.getFreeContainers(params).then(result => context.commit('setSearchResults', result))
      }
    }
  },
  mutations: {
    setContainerTypes (state, types) {
      state.types = types
    },
    setSearchParams (state, params) {
      state.params = params
    },
    setSearchResults (state, results) {
      state.results = results
    }
  }
})
