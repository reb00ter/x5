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
    }
  },
  mutations: {
    setContainerTypes (state, types) {
      console.log('commit')
      state.types = types
    }
  }
})
