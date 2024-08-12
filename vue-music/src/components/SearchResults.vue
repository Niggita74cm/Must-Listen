<!--НАДО ДОБАВИТЬ ЧТОБЫ БЫЛ ВЫВОД И ОБЩИЙ РЕЙТИНГ ПОПУЛЯРНОСТИ И РЕЙТИНГ ПОПУЛЯРНОСТИ ЧТО НА САЙТЕ ФОРМИРУЕТСЯ-->

<template>
    <div id="app">
      <div class="menu-row">
        <MenuBarAuth />
      </div>
      <div>
        <h2>Результаты поиска</h2>
        <p v-if="searchTerm">Вы искали: "{{ searchTerm }}"</p>
        <table v-if="searchResults.length" class="centered-table">
          <thead>
            <tr>
              <th>Название трека</th>
              <th>Название альбома</th>
              <th>Исполнитель</th>
              <th>Оценка</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="result in searchResults"
              :key="result.track_id"
              @click="goToMusicPage(result)"
              class="clickable-row"
            >
              <td>{{ result.track_name }}</td>
              <td>{{ result.album_name }}</td>
              <td>{{ result.artists }}</td>
              <td>{{ result.rating }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else>Ничего не найдено</p>
      </div>
    </div>
  </template>
  
  <script>
  import MenuBarAuth from './MenuBarAuth.vue';
  import axios from "axios";
  export default {
    name: 'SearchResults',
    components: {
      MenuBarAuth,
    },
    computed: {
      searchTerm() {
        ///this.$route.query.q ЭТО ТО ЧТО ПОЛЬЗОВАТЕЛЬ ВВЕЛ В ПОИСК 
        return this.$route.query.NameTrack || '';
      },
    },
    data() {
      return {
        ///СПИСОК С СЕРВЕРА
        searchResults: [],
      };
    },
    methods: {
      goToMusicPage(result) {
        this.$router.push({ name: 'MusicPage', params: { track_id: result.track_id } });
      },
      getFoundTracks(){
        axios.get(`/SearchResults?NameTrack=${this.$route.query.NameTrack}`)
          .then((res) => {
            this.searchResults = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
    created() {
      this.getFoundTracks();
    },
  };
  </script>
  
  <!-- Стили остались без изменений -->
  <style>
.centered-table {
  margin: 0 auto;
  border-collapse: collapse;
  text-align: center;
  font-size: 1.2rem;
}

.centered-table th,
.centered-table td {
  padding: 10px 20px;
  border-bottom: 1px solid #ddd;
}

.clickable-row {
  cursor: pointer;
}
</style>