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
              <td>{{ result.popularity }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else>Ничего не найдено</p>
      </div>
    </div>
  </template>
  
  <script>
  import MenuBarAuth from './MenuBarAuth.vue';
  
  export default {
    name: 'SearchResults',
    components: {
      MenuBarAuth,
    },
    computed: {
      searchTerm() {
        ///this.$route.query.q ЭТО ТО ЧТО ПОЛЬЗОВАТЕЛЬ ВВЕЛ В ПОИСК 
        return this.$route.query.q || '';
      },
    },
    data() {
      return {
        ///СПИСОК С СЕРВЕРА
        searchResults: [
          {
            track_id: 1,
            track_name: 'Wolves',
            album_name: 'The Life Of Pablo',
            artists: 'Kanye West',
            popularity: 5,
          },
          {
            track_id: 2,
            track_name: 'Black Skinhead',
            album_name: 'Yeezus',
            artists: 'Kanye West',
            popularity: 4,
          },
          {
            track_id: 3,
            track_name: 'Серпантин',
            album_name: 'Great Depression',
            artists: 'Markul',
            popularity: 3,
          },
          {
            track_id: 4,
            track_name: 'False Alarm',
            album_name: 'Starboy',
            artists: 'The Weeknd',
            popularity: 4,
          },
          {
            track_id: 5,
            track_name: 'Положение',
            album_name: 'Уроборос: Улица 36',
            artists: 'Скриптонит',
            popularity: 5,
          },
          {
            track_id: 6,
            track_name: 'FUK SUMN',
            album_name: 'VULTURES 1',
            artists: 'Kanye West',
            popularity: 4,
          },
          {
            track_id: 7,
            track_name: 'Chlorine',
            album_name: 'Trench',
            artists: 'Twenty One Pilots',
            popularity: 3.8,
          },
        ],
      };
    },
    methods: {
      goToMusicPage(result) {
        this.$router.push({ name: 'MusicPage', params: { id: result.id } });
      },
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