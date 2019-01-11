<template>
    <div class="social_auth">
      <div class="social_auth__provider social_auth__vk"><a href="/auth/login/vk-oauth2">VK</a> </div>
      <dx-button :text="text"/>
    </div>
</template>

<script>
import DxButton from 'devextreme-vue/button'
export default {
  name: 'SocialAuth',
  data () {
    return {
      text: 'test'
    }
  },
  components: {
    DxButton
  }
}
</script>

<style scoped>

</style>
