<template>
  <div id="app">

      <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

  },
};
</script>

<style>
.navbar,
.navbar-brand {
  font-size: 16pt;
}

footer {
  font-size: 16pt;
}

.content-container {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Равные ширины для обеих колонок */
  gap: 20px; /* Отступ между колонками */
}

.image-row {
  /* Стили для компонента ImageRow */
}

.auth-user {
  max-width: 400px; /* Максимальная ширина контейнера формы */
  margin: 0 auto; /* Центрирование контейнера */
  padding: 20px; /* Отступы внутри контейнера */
  background-color: #f5f5f5; /* Цвет фона контейнера */
  border-radius: 5px; /* Скругленные углы */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Тень */
  /* Стили для компонента AuthUser */
}
</style>

<!--<template>-->
<!--  <div id="app">-->
<!--    <router-view/>-->
<!--  </div>-->
<!--</template>-->

<!--<style>-->
<!--#app {-->
<!--  font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--}-->
<!--</style>-->