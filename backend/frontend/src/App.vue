<template>
  <div id="app">
    <Hero/>
    <MovieList/>
  </div>
</template>

<script>
import Hero from "./components/layout/Hero.vue";
import MovieList from "./components/layout/MovieList";

export default {
  name: "app",
  components: {
    Hero,
    MovieList
  }
};
</script>

<style>
#app {
  min-height: 100vh;
  padding: 0;
  margin: 0;
}
</style>
