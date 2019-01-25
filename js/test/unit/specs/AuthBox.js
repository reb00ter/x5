import Vue from 'vue'
import AuthBox from '@/components/AuthBox.vue'

describe('AuthBox.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(AuthBox)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.social_auth__vk').textContent)
      .toEqual('VK')
  })
})
