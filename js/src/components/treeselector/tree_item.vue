<template>
    <li>
        <div v-if="leaf.children" class="tree_switch"><div class="expander" :class="{opened: leaf.opened}" @click="switchLeaf(leaf)"></div></div>
        <input type="checkbox" :id="leaf.type+'_'+leaf.id" @change="changed" v-model="checked">
        <label :for="leaf.type+'_'+leaf.id">{{ leaf.title }}</label>
        <ul v-if="leaf.children" v-show="leaf.opened">
            <tree_item v-for="child in leaf.children" :key="child.type+child.id" v-bind:leaf="child" @change="changed" v-if="child.visible" :title="child.type+child.id"/>
        </ul>
    </li>
</template>

<script>
export default {
  name: 'tree_item',
  props: [
    'leaf'
  ],
  methods: {
    changed: function () {
      this.$emit('change')
    },
    switchLeaf: function (leaf) {
      this.$store.commit('switchLeaf', leaf)
    }
  },
  computed: {
    checked: {
      get () {
        return this.leaf.checked
      },
      set (value) {
        value ? this.$store.commit('checkLeaf', this.leaf) : this.$store.commit('uncheckLeaf', this.leaf)
      }
    }
  }
}
</script>

<style scoped>
  .tree_switch{
    display: inline-block;
  }
  .expander{
    width: 14px;
    height: 14px;
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNCcgaGVpZ2h0PScxNCc+PGcgY2xhc3M9J2N1cnJlbnRMYXllcicgc3R5bGU9Jyc+PHBhdGggZmlsbD0nI2ZmODAwMCcgc3Ryb2tlPScjMDAwMDAwJyBzdHJva2Utd2lkdGg9JzAuNCcgc3Ryb2tlLWxpbmVqb2luPSdyb3VuZCcgZD0nTTAsMCBMMCwxNCBMOSw3IEwwLDAgeicgZmlsbC1vcGFjaXR5PScxJy8+PC9nPjwvc3ZnPg==");
  }
  .expander.opened{
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNCcgaGVpZ2h0PScxNCc+PGcgY2xhc3M9J2N1cnJlbnRMYXllcicgc3R5bGU9Jyc+PHBhdGggZmlsbD0nI2ZmODAwMCcgc3Ryb2tlPScjMDAwMDAwJyBzdHJva2Utd2lkdGg9JzAuNCcgc3Ryb2tlLWxpbmVqb2luPSdyb3VuZCcgZD0nTTAsNCBMMTQsNCBMNywxNCBMMCw0IHonIGZpbGwtb3BhY2l0eT0nMScvPjwvZz48L3N2Zz4=");
  }
  ul{
    padding-left: 0px
  }
  li{
    list-style-type: none;
    margin-left: 15px;
  }
</style>
