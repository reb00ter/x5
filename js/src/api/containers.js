const axios = require('axios')
const axiosConfig = {
  baseURL: '/api'
}

const HTTP = axios.create(axiosConfig)

export default {
  async getCurrentUser () {
    try {
      let resp = await HTTP.get('users/current')
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getContainerTypes () {
    try {
      let resp = await HTTP.get('containers/types')
      return await resp.data
    } catch (e) {
      return {}
    }
  }
}
