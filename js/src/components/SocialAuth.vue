<template>
  <div class="social_auth">
    <a href="/accounts/login">Авторизоваться</a>
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
