<template>
  <section class="hero is-black is-medium">
    <!-- Hero head: will stick at the top -->
    <div class="hero-head">
      <Nav/>
    </div>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="subtitle">무비무비가 추천하는 오늘의 영화</h2>
      </div>
    </div>
  </section>
</template>

<script>
import Nav from "./Nav.vue";

export default {
  name: "Hero",
  components: { Nav }
};
</script>

<style scoped>
.subtitle {
  font-family: "Gugi";
}
</style>
