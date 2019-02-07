<template>
  <div id="app">
    <div class="page">
      <div class="page-header">
        <div class="container">
          <b-navbar toggleable="lg" type="light">
            <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
            <b-navbar-brand href="#">Контейнеры</b-navbar-brand>
            <b-collapse is-nav id="nav_collapse">
              <main-menu :auth_done="user.id !== null"/>
            </b-collapse>
            <auth-box :user="user"/>
          </b-navbar>
        </div>
      </div>
    </div>
    <router-view/>
    <b-modal hide-footer title="Добавить свободные контейнеры" v-model="showAddFree">
      <dx-form :items="freeFormSpec" labelLocation="top" :colCount="2" :formData="freeFormData"/>
      <dx-button text="Добавить" @click="createFree"/>
      <dx-button text="Отмена" @click="showAddFree=false"/>
    </b-modal>
    <b-modal hide-footer title="Добавить требуемые контейнеры" v-model="showAddNeed">
      <dx-form :items="needFormSpec" labelLocation="top" :colCount="2" :formData="needFormData"/>
      <dx-button text="Добавить" @click="createNeed"/>
      <dx-button text="Отмена" @click="showAddNeed=false"/>
    </b-modal>
  </div>
</template>

<script>
import api from './api/containers'
import AuthBox from './components/AuthBox.vue'
import MainMenu from './components/MainMenu.vue'
import bModal from 'bootstrap-vue/es/components/modal/modal'
import DxButton from 'devextreme-vue/button'
import DxForm from 'devextreme-vue/form'
import bNavbar from 'bootstrap-vue/es/components/navbar/navbar'
import bCollapse from 'bootstrap-vue/es/components/collapse/collapse'
import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand'
import bNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav'
import bNavbarToggle from 'bootstrap-vue/es/components/navbar/navbar-toggle'

export default {
  name: 'App',
  components: {
    bNavbar,
    bCollapse,
    bNavbarBrand,
    bNavbarNav,
    bNavbarToggle,
    bModal,
    DxButton,
    DxForm,
    MainMenu,
    AuthBox
  },
  computed: {
    user () {
      return this.$store.state.user
    },
    showAddFree: {
      get () {
        return this.$store.state.showAddFree
      },
      set (value) {
        this.$store.commit('showAddFree', value)
      }
    },
    showAddNeed: {
      get () {
        return this.$store.state.showAddNeed
      },
      set (value) {
        this.$store.commit('showAddNeed', value)
      }
    }
  },
  data () {
    return {
      freeFormData: {
        parts: true
      },
      freeFormSpec: [
        {
          colSpan: 2,
          dataField: 'type',
          label: {
            text: 'Тип'
          },
          editorType: 'dxSelectBox',
          editorOptions: {
            dataSource: '/api/containers/types/',
            valueExpr: 'id',
            displayExpr: 'title',
            searchEnabled: true
          }
        },
        {
          dataField: 'count',
          label: {
            text: 'Количество'
          },
          editorType: 'dxNumberBox',
          editorOptions: {
            min: 1
          }
        },
        {
          dataField: 'parts',
          label: {
            text: 'Можно частями'
          },
          editorType: 'dxCheckBox'
        },
        {
          colSpan: 2,
          dataField: 'location',
          label: {
            text: 'Расположение'
          },
          editorType: 'dxSelectBox',
          editorOptions: {
            dataSource: '/api/stations/',
            valueExpr: 'id',
            displayExpr: 'title',
            searchEnabled: true
          }
        },
        {
          colSpan: 2,
          dataField: 'address',
          label: {
            text: 'Адрес'
          },
          editorType: 'dxTextBox'
        },
        {
          dataField: 'date_from',
          label: {
            text: 'С'
          },
          editorType: 'dxDateBox',
          editorOptions: {
            value: null,
            width: '100%'
          }
        },
        {
          dataField: 'date_till',
          label: {
            text: 'По'
          },
          editorType: 'dxDateBox',
          editorOptions: {
            value: null,
            width: '100%'
          }
        }
      ],
      needFormData: {},
      needFormSpec: [
        {
          dataField: 'type',
          label: {
            text: 'Тип'
          },
          editorType: 'dxSelectBox',
          editorOptions: {
            dataSource: '/api/containers/types/',
            valueExpr: 'id',
            displayExpr: 'title',
            searchEnabled: true
          }
        },
        {
          dataField: 'count',
          label: {
            text: 'Количество'
          },
          editorType: 'dxNumberBox',
          editorOptions: {
            min: 1
          }
        },
        {
          colSpan: 2,
          dataField: 'location',
          label: {
            text: 'Расположение'
          },
          editorType: 'dxSelectBox',
          editorOptions: {
            dataSource: '/api/stations/',
            valueExpr: 'id',
            displayExpr: 'title',
            searchEnabled: true
          }
        },
        {
          colSpan: 2,
          dataField: 'address',
          label: {
            text: 'Адрес'
          },
          editorType: 'dxTextBox'
        },
        {
          dataField: 'date_from',
          label: {
            text: 'С'
          },
          editorType: 'dxDateBox',
          editorOptions: {
            value: null,
            width: '100%'
          }
        },
        {
          dataField: 'date_till',
          label: {
            text: 'По'
          },
          editorType: 'dxDateBox',
          editorOptions: {
            value: null,
            width: '100%'
          }
        }
      ]
    }
  },
  methods: {
    auth: function () {
      this.$router.push('auth')
    },
    createFree: function () {
      let vue = this
      api.storeFreeContainers(this.freeFormData).then(function (data) {
        vue.showAddFree = false
      })
    },
    createNeed: function () {
      let vue = this
      api.storeNeedContainers(this.needFormData).then(function (data) {
        vue.showAddNeed = false
      })
    }
  },
  created: function () {
    let app = this
    api.getCurrentUser().then(function (data) {
      app.$store.commit('setUser', data)
    })
  }
}
</script>

<style>
.logo{
  background-image: url("./assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
}
.auth{
  float: right;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
