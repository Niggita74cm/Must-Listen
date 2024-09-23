<template>
  <div id="app">
    <header class="bg-dark">
      <b-navbar class="w-9 mx-auto slim-navbar" type="dark" variant="dark">
        <b-navbar-brand href="#">
          <img src="./logo/logo.png" alt="Must Listen Logo" class="logo">
        </b-navbar-brand>
        <b-navbar-brand>Must Listen</b-navbar-brand>
        <b-navbar-nav>
          <!-- <b-nav-item href="#">Вход</b-nav-item>
          <b-nav-item href="#">Регистрация</b-nav-item>-->
        </b-navbar-nav>
      </b-navbar>
    </header>
  </div>
</template>

<script>
export default {
  name: 'MenuSidebar',
}
</script>

<style>
.slim-navbar {
  height: 60px; /* Установите желаемую высоту, например, 40px */
}
</style>
