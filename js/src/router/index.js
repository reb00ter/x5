import Vue from 'vue'
import Router from 'vue-router'
import SocialAuth from '@/components/SocialAuth'
import IndexPage from '@/components/IndexPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexPage
    },
    {
      path: '/auth',
      name: 'SocialAuth',
      component: SocialAuth
    }
  ]
})
