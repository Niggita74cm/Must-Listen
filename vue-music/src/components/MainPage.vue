<template>
  <div id="app">
    <div class="menu-row">
      <MenuBarAuth />
    </div>

    <div class="main-title-container">
      <h1 class="main-title">Добро пожаловать в Must Listen!</h1>
    </div>
    <div class="sorting-container">
      <span class="sorting-label">Сортировка:</span>
      <button class="sorting-button active" @click="toggleSortButton($event.target)">Популярное</button>
      <button class="sorting-button" @click="toggleSortButton($event.target)">Мои оценки</button>
      <button class="sorting-button" @click="toggleSortButton($event.target)">Мои комментарии</button>
    </div>
    <div v-if="sortedResults.length" class="table-container">
      <table class="centered-table">
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
            v-for="result in sortedResults"
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
    </div>
    <div v-else class="no-results">Ничего не найдено</div>
  </div>
</template>

<script>
import MenuBarAuth from './MenuBarAuth.vue';
import axios from "axios";
export default {
  name: 'App',
  components: {
    MenuBarAuth,
  },
  data() {

    return {
      //ИЗНАЧАЛЬНО ПРИСЫЛАЕМ ОТСОРТИРОВАННОЕ ПО ПОПУЛЯРНОСТИ ТЕ ПО ОЦЕНКЕ
      sortedResults: [],
      InfoAboutTypePageTracks: {
        TypeSorting: 'date_down',
        NumberPage: 1
      }
    };
  },
  methods: {
    getUserTracks(){
      axios.get(`/MainPage?NumberPage=${this.InfoAboutTypePageTracks.NumberPage}&TypeSorting=${this.InfoAboutTypePageTracks.TypeSorting}`)
          .then((res) => {
            this.sortedResults = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    goToMusicPage(result) {
        this.$router.push({ name: 'MusicPage', params: { id: result.id } });
      },
    sortByPopularity() {
      //ТАК СОРТИРОВКА ПО ПОПУЛЯРНОСТИ(ПО ОЦЕНКАМ В ОБЩЕМ)
      this.sortedResults = this.sortedResults.slice().sort((a, b) => b.popularity - a.popularity);
    },
    sortByMyRatings() {
      //ТАК СОРТИРОВКА ПО ПОПУЛЯРНОСТИ(ПО ОЦЕНКАМ ТОЛЬКО ПОЛЬЗОВАТЕЛЯ)
    },
    sortByData() {
      //ТАК СОРТИРОВКА ПО ПОПУЛЯРНОСТИ(ПО ДАТЕ)
    },
    toggleSortButton(button) {
      const buttons = document.querySelectorAll('.sorting-button');
      buttons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');

      const buttonText = button.textContent.trim();
      
      if (buttonText === 'Популярное') {
        this.sortByPopularity();
      } else if (buttonText === 'Мои оценки') {
        this.sortByMyRatings();
      } else if (buttonText === 'Мои комментарии') {
        this.sortByData();
      }
    },
  },
  created() {
        this.getUserTracks();
  },
};
</script>


  
  <style>
.content-container {
  position: relative;
  width: 100vw;
  height: calc(100vh /* - высота MenuBarAuth */);
}

.main-title-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  pointer-events: none;
  margin-top: 60px; 
}

.main-title {
  font-size: 3rem;
  color: #4c4949;
  text-shadow: 1px 1px 2px rgba(118, 109, 109, 0.3);
}


.table-container {
  margin-top: 20px;
  padding: 0 20px;
  
  margin-right: 500px; /* Добавляем левый отступ */
}

.centered-table {
  width: 150%;
  border-collapse: separate;
  text-align: center;
  border-spacing: 0;
}

.centered-table th,
.centered-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.centered-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.centered-table tbody tr:hover {
  background-color: #f5f5f5;
  cursor: default;
}


.sorting-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 90px;
}

.sorting-label {
  margin-right: 10px;
  font-weight: bold;
  font-size: 1.2rem;
}

.sorting-button {
  margin-left: 10px;
  padding: 8px 16px;
  background-color: #898686;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.sorting-button:hover {
  background-color: #6d6a6a;
}
.sorting-button.active {
  background-color: #3a3a3a;
  color: #fff;
}
.no-results {
  text-align: center;
  font-size: 18px;
  color: #888;
  margin-top: 20px;
}


</style>
  