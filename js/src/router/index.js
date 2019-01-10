import Vue from 'vue'
import Router from 'vue-router'
import SocialAuth from '@/components/SocialAuth'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SocialAuth',
      component: SocialAuth
    }
  ]
})
