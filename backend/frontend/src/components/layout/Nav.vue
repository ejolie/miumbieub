<template>
  <nav class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item">
          <!-- <img src="https://bulma.io/images/bulma-type-white.png" alt="Logo"> -->
          ㅁㅂㅁㅂ
        </a>
        <span class="navbar-burger burger" data-target="navbarMenuHeroA">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
      <div id="navbarMenuHeroA" class="navbar-menu">
        <div class="navbar-end">
          <a class="navbar-item is-active">홈</a>
          <a class="navbar-item">검색</a>
          <span class="navbar-item">
            <a class="button is-primary">
              <span>회원가입</span>
            </a>
          </span>
          <span class="navbar-item">
            <a class="button is-light">
              <span>로그인</span>
            </a>
          </span>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Nav"
};
</script>

<style scoped>
.navbar-brand .navbar-item {
  font-family: "Gugi", cursvie;
}

.navbar-end .navbar-item {
  font-family: "Noto Sans KR", sans-serif;
  font-weight: 400;
}
</style>
