const axios = require('axios')
const axiosConfig = {
  baseURL: '/api'
}

const HTTP = axios.create(axiosConfig)

export default {
  async getCurrentUser () {
    try {
      let resp = await HTTP.get('users/current/')
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getLocations () {
    try {
      let resp = await HTTP.get('locations/')
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getContainerTypes () {
    try {
      let resp = await HTTP.get('containers/types/')
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getFreeContainers (params) {
    try {
      let resp = await HTTP.get('containers/free/', {params: params})
      return await resp.data
    } catch (e) {
      return {}
    }
  }
}
