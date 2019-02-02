const axios = require('axios')

function formatDate (date) {
  return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`
}

// функция формирования параметров для GET запроса из переданного словаря
const transformRequestOptions = params => {
  let options = ''
  for (const key in params) {
    if (typeof params[key] !== 'object' && params[key]) {
      options += `${key}=${params[key]}&`
    } else if (typeof params[key] === 'object' && params[key] && params[key].length) {
      params[key].forEach(el => {
        options += `${key}=${el}&`
      })
    } else if (typeof params[key] === 'object' && key.includes('date') && params[key]) {
      options += `${key}=${formatDate(params[key])}&`
    }
  }
  return options ? options.slice(0, -1) : options
}

const axiosConfig = {
  baseURL: '/api',
  paramsSerializer: params => transformRequestOptions(params),
  // `xsrfCookieName` is the name of the cookie to use as a value for xsrf token
  xsrfCookieName: 'SecretCSRFCo0kie', // default
  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'SecretCSRFHeader' // default
}
axios.defaults.xsrfCookieName = 'SecretCSRFCo0kie'
axios.defaults.xsrfHeaderName = 'X-SecretCSRFHeader'

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
  },
  async storeFreeSearchParams (params) {
    try {
      let resp = await HTTP.post('search/free/', params)
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getMyFreeSearchParams () {
    try {
      let resp = await HTTP.get('search/free/')
      return await resp.data
    } catch (e) {
      return {}
    }
  },
  async getFreeSearchParams (id) {
    try {
      let resp = await HTTP.get('search/free/' + id + '/')
      return await resp.data
    } catch (e) {
      return {}
    }
  }
}
