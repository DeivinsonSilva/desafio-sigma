<template>
  <div id="app">
    <!--img alt="Vue logo" src="./assets/logo.png"-->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Quote/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Quote from './components/Quote.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Quote
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #4582ec;
  margin-top: 20px;

  display: flex;
  flex-direction: column;
  align-items: center;

}
</style>
