<template>
  <div id="app">
    <MenuBar />
    <div class="back-link-container">
      <router-link to="/MainPage" class="back-link">
        <b-icon icon="arrow-left" aria-label="Previous"></b-icon>
      </router-link>
    </div>
  </div>
</template>

<script>
import MenuBar from './MenuBar.vue';

export default {
  name: 'App',
  components: {
    MenuBar
  }
}
</script>

<style scoped>
.back-link-container {
  display: flex;
  margin-top: 1rem;
  margin-left: 1rem; /* Добавили отступ слева */
}

.back-link {
  text-decoration: none;
  color: #333;
  font-size: 2rem; /* Увеличили размер иконки */
  font-weight: 900;
}
</style>
