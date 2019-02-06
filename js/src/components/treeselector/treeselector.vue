<template>
    <div class="tree-selector">
        <ul class="selection" @click="set_focus">
            <li class="selected-item" v-for="item in selected" :key="item.id" @click="uncheck(item)">{{ item.title }}</li>
            <li class="input"><input type="text" v-model="query" title="фильтр"></li>
        </ul>
        <ul class="suggestions" :style="suggestion_size">
            <tree-item v-for="elem in filtered_options" :key="elem.type+elem.id" :leaf="elem" @change="update_selected" v-if="elem.visible"/>
        </ul>
    </div>
</template>

<script>
import TreeItem from './tree_item.vue'

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
        let vue = this
        this.options.forEach(function (item) {
          if (vue.filterTree(item, expression)) {
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
        let vue = this
        this.options.forEach(function addSelected (option) {
          vue.addIfChecked(result, option)
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
    },
    'addIfChecked': function (list, option) {
      if (option.checked) {
        list.push(option)
      } else {
        if (option.children) {
          let vue = this
          option.children.forEach(function (elem) {
            vue.addIfChecked(list, elem)
          })
        }
      }
    },
    'showAllChildren': function (root) {
      if (root.children == null) {
        return
      }
      let vue = this
      root.children.forEach(function (item) {
        vue.$store.commit('showLeaf', item)
        if (item.children == null) {
          return
        }
        vue.showAllChildren(item)
      })
    },
    'filterTree': function (root, expression) {
      if (root.title.match(new RegExp(expression, 'i'))) {
        this.$store.commit('showLeaf', root)
        this.$store.commit('closeLeaf', root)
        this.showAllChildren(root)
        return true
      }
      let gotVisible = false
      if (root.children) {
        let vue = this
        root.children.forEach(function (item) {
          gotVisible = vue.filterTree(item, expression) || gotVisible
        })
        gotVisible ? this.$store.commit('openLeaf', root) : this.$store.commit('closeLeaf', root)
      }
      gotVisible ? this.$store.commit('showLeaf', root) : this.$store.commit('hideLeaf', root)
      return gotVisible
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
    font-size: 14px;
  }
  .suggestions{
    display: none;
    position: absolute;
    background-color: white;
    outline: 1px solid black;
    z-index: 100;
    height: 200px;
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
    width: 125px;
  }
  ul{
    padding-left: 0px
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
