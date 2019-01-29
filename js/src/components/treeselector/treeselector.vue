<template>
    <div class="tree-selector">
        <ul class="selection" @click="set_focus">
            <li class="selected-item" v-for="item in selected" :key="item.id" @click="uncheck(item)">{{ item.title }}</li>
            <li class="input"><input type="text" v-model="query" title="фильтр"></li>
        </ul>
        <ul class="suggestions" :style="suggestion_size">
            <tree-item v-for="elem in filtered_options" :key="elem.type+elem.id" v-bind:leaf="elem" @change="update_selected" v-if="elem.visible"/>
        </ul>
    </div>
</template>

<script>
import TreeItem from './tree_item.vue'
import Vue from 'vue'

function addIfChecked (list, option) {
  if (option.checked) {
    list.push(option)
  } else {
    if (option.children) {
      option.children.forEach(function (elem) {
        addIfChecked(list, elem)
      })
    }
  }
}

function showAllChildren (root) {
  if (root.children == null) {
    return
  }
  root.children.forEach(function (item) {
    Vue.set(item, 'visible', true)
    if (item.children == null) {
      return
    }
    showAllChildren(item)
  })
}

function filterTree (root, expression) {
  if (root.title.match(new RegExp(expression, 'i'))) {
    Vue.set(root, 'visible', true)
    Vue.set(root, 'opened', false)
    showAllChildren(root)
    return true
  }
  let gotVisible = false
  if (root.children) {
    root.children.forEach(function (item) {
      gotVisible = filterTree(item, expression) || gotVisible
    })
    Vue.set(root, 'opened', gotVisible)
  }
  Vue.set(root, 'visible', gotVisible)
  return gotVisible
}

export default {
  name: '',
  data: function () {
    return {
      query: '',
      selected: [],
      suggestion_size: {
        width: '1000px',
        top: '39px'
      }
    }
  },
  updated: function () {
    this.suggestion_size.width = this.$el.offsetWidth + 'px'
    this.suggestion_size.top = this.$el.offsetHeight + 'px'
  },
  computed: {
    filtered_options: function () {
      if (this.options) {
        let queryParts = this.query.split(/ |,|\./g)
        let expression = queryParts.join('.*')
        let result = []
        this.options.forEach(function (item) {
          if (filterTree(item, expression)) {
            result.push(item)
          }
        })
        return result
      }
      return []
    }
  },
  props: [
    'options'
  ],
  methods: {
    'update_selected': function () {
      let result = []
      if (this.options) {
        this.options.forEach(function addSelected (option) {
          addIfChecked(result, option)
        })
      }
      this.selected = result
      this.$emit('change', this.selected)
    },
    'update': function () {
      this.$forceUpdate()
    },
    'uncheck': function (item) {
      item.checked = false
      this.update_selected()
    },
    'set_focus': function () {
      this.$el.querySelector('input[type=text]').focus()
    }
  },
  components: {
    TreeItem
  }
}
</script>

<style scoped>
  input{
    outline: none;
  }
  .tree-selector{
    position: relative;
    text-align: left;
    font-size: 12px;
  }
  .suggestions{
    display: none;
    position: absolute;
    background-color: white;
    outline: 1px solid black;
    z-index: 100;
    height: 300px;
    margin-left: 0;
    overflow: auto;
  }
  .tree-selector:focus-within .suggestions,
  .tree-selector:hover .suggestions{
    display: block;
  }
  .tree-selector {
    border: 1px solid #ddd;
    border-radius: 4px;
    background: #fefefe;
  }
  .tree-selector input{
    box-shadow: none;
    transition: none;
    border: none;
    border-radius: 0;
    margin: 0;
    padding: 4px 5px;
  }
  ul{
    padding-left: 20px
  }
  li{
    list-style-type: none;
    margin-left: 5px;
  }
  ul.selection{
    margin-bottom: 0;
    padding-left: 0;
  }
  ul.selection li{
    margin-left: 5px;
    display: inline-block;
    cursor: default;
  }
  ul.selection li.selected-item {
    border-radius: 7px;
    padding: 2px 20px 2px 10px;
    background-color: #ff8300;
  }
</style>
