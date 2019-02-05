<template>
  <b-navbar-nav>
    <b-nav-item><router-link :to="{ name: 'index' }">Главная</router-link></b-nav-item>
    <b-nav-item v-if="auth_done"><router-link :to="{ name: 'StoredFilters' }">Сохранённые фильтры</router-link></b-nav-item>
    <b-nav-item-dropdown  v-if="auth_done" id="nav7_ddown" text="Добавить контейнер" extra-toggle-classes="nav-link-custom" right>
      <b-dropdown-item>Свободный</b-dropdown-item>
      <b-dropdown-item>Искомый</b-dropdown-item>
    </b-nav-item-dropdown>
  </b-navbar-nav>
</template>

<script>
import bNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav'
import bNavItem from 'bootstrap-vue/es/components/nav/nav-item'
import bNavItemDropDown from 'bootstrap-vue/es/components/nav/nav-item-dropdown'
import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item'

export default {
  name: 'MainMenu',
  props: ['auth_done'],
  components: {
    bNavbarNav,
    bNavItem,
    bNavItemDropDown,
    bDropdownItem
  }
}
</script>

<style scoped>

</style>
