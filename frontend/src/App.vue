<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  name: 'App',
  components: {Header}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.my-card {
  background-color: #eae8d8;
  background-size: 100%;
}

.my-card2 {
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}
</style>
