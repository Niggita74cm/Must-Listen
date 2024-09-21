<!--КАКИЕ ДАННЫЕ О КАРТИНКЕ ПЕРЕДОВАТЬ, БЕК НЕ ПОНИМАТЬ, ПОЭТОМУ ЭТО НЕ ПРИКОНЕКЧЕНО -->
<!--НАДО ДОБАВИТЬ ЧТОБЫ БЫЛ ВЫВОД И ОБЩИЙ РЕЙТИНГ ПОПУЛЯРНОСТИ И РЕЙТИНГ ПОПУЛЯРНОСТИ ЧТО НА САЙТЕ ФОРМИРУЕТСЯ-->

<!--ВОЗМОЖНО СТОИТ ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯМ ИЗМЕНЕНИЕ  СВОИХ КОММЕНТАРИЕВ -->
<template>
    <div id="app">
      <div class="menu-row">
        <MenuBarAuth />
      </div>
      <div class="track-info">
        <div class="track-image">
          <a :href="images[0].link" target="_blank">
            <img :src="images[0].url" :alt="images[0].alt" />
          </a>
        </div>
        <div class="track-details">
          <div class="track-title">
            <h2>{{ Musicinfo.track_name }}</h2>
          </div>
          <div class="track-meta">
            <p><b>Альбом</b> {{ Musicinfo.album_name }}</p>
            <p><b>Исполнитель</b> {{ Musicinfo.artists }}</p>
            <p><b>Рейтинг</b> {{ Musicinfo.rating }}</p>
            <p><b>Продолжительность</b> {{ formatDuration(Musicinfo.duratind_ms) }}</p>
            <p>
              <b>Поставить оценку</b>
              <select v-model="rating1" class="rating-select">
                <option v-for="rating in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :value="rating" :key="rating">{{ rating }}</option>
              </select>
              <button @click="submitRating" class="rating-button">Оценить</button>
            </p>
            <p v-if="Musicinfo.userRating">Ваша оценка {{ Musicinfo.userRating }}</p>
          </div>
        </div>

        <div class="comment-form">
        <textarea v-model="newComment" placeholder="Введите комментарий" rows="3"></textarea>
        <button @click="addComment">Комментировать</button>
      </div>
   



      </div>
      <div class="comments-about">
        <h3>Комментарии</h3>
        <div v-for="(comment, index) in track_comments" :key="index" class="comment">
          
          <div class="comment-content">
            <p>
              <strong>{{ comment.user_name }}</strong> <code style="color:grey;">{{ comment.time }}</code>
              <br/>
              {{ comment.text_comment }}
            </p>

          </div>

        <button
            v-if="comment.user_name === username || NumberPrivileges === 'admin'"
            @click="removeComment(index, comment.comment_id)"
            class="delete-button"
          >
            Удалить
          </button>

          <hr v-if="index !== track_comments.length - 1">
        </div>
      </div>
    </div>
  </template>

  <script>
  import MenuBarAuth from './MenuBarAuth.vue';
  import axios from "axios";
  export default {
    name: 'MusicPage',
    components: {
      MenuBarAuth,
    },
    computed: {
      musicId() {
        const trackId=this.$route.params.track_id;
        sessionStorage.setItem('track_id', trackId);
        return this.$route.params.track_id; ///ЭТО ID ТРЕКА ПО КОТОРОМУ КЛИКНУЛИ
      },
    },
    data() {
      return {

        rating1: null,
        username: '', //ЕСЛИ admin БУДЕТ КНОПКА УДАЛИТЬ
        NumberPrivileges: '',
        ///ДАННЫЕ О ТРЕКЕ ТОЖЕ НУЖНЫ С СЕРВЕРА
        Musicinfo: {
            track_id: null,
            userRating: null, ///ЕСЛИ ПОСТАВЛЕНА ТО ПЕРЕДАТЬ СЮДА
            track_name: '',
            album_name: '',
            artists: '',
            rating: 0.0,
            popularity: 0,
            duratind_ms: 0,
            url_images: ''
        },
        //КАРТИНОЧКА С СЕРВЕРА
        images: [
          { id: 1, url: 'https://avatars.yandex.net/get-music-content/41288/5c92aeb1.a.3555472-1/m1000x1000', alt: 'Image 1', link: 'https://music.yandex.ru/album/3555472' },
        ],
        //КОММЕНТАРИИ С СЕРВЕРА
        track_comments: [
          {
            comment_id: 1,
            user_name: 'sasha0021',
            time: "23.04.2024",
            text_comment: '👍',
          },
        ],
        FormPostRequest:{
          track_id: 0,
          rating: 0,
          comment: '',
          command: '',
          comment_id: 0
        },
        FormPostResponse:{
          errors: '',
          date: '',
          comment_rating_id: 0
        }
    };
  },
  methods: {
    formatDuration(durationMs) {
      const minutes = Math.floor(durationMs / 60000);
      const seconds = Math.floor((durationMs % 60000) / 1000);
      return `${minutes}:${seconds.toString().padStart(2, '0')}`;
    },
getTrackInfo(){
      if (this.$route.params.track_id !== undefined){
        sessionStorage.setItem('track_id', this.$route.params.track_id);
      }
      const trackId = sessionStorage.getItem('track_id'); // берем track_id из маршрута
      axios.get(`/MusicPage`, { params: { track_id: trackId } }) // используем правильный синтаксис
          .then((res) => {
            this.Musicinfo.track_id=res.data.track_id;
            this.Musicinfo.track_name=res.data.track_name;
            this.Musicinfo.album_name=res.data.album_name;
            this.Musicinfo.artists=res.data.artists;
            this.Musicinfo.rating=res.data.rating;
            this.Musicinfo.popularity=res.data.popularity;
            this.Musicinfo.duratind_ms=res.data.duratind_ms;
            this.Musicinfo.url_images=res.data.url_images;
            this.Musicinfo.userRating=res.data.userRating;
            this.track_comments=res.data.track_comments;
            this.username=res.data.username;
            this.NumberPrivileges = res.data.NumberPrivileges;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    submitRating() {
      this.FormPostRequest.command = 'Set Rating';
      this.FormPostRequest.rating=this.rating1;
      this.FormPostRequest.track_id = sessionStorage.getItem('track_id');
      const data = JSON.stringify(this.FormPostRequest);
      axios.post('/MusicPage', data, {
        headers: {
          'Content-Type': 'application/json',
        }
      })
      .then((response) => {
        if(response.data.errors===''){
          this.Musicinfo.userRating = this.rating1;
          console.log('Rating:', this.Musicinfo.userRating);
        }
        else{
          console.log('Errors server set rating');
        }
      })
      .catch((error) => {
        console.error('Set Rating:', error);
      });


    },
    addComment() {
    //Здесь надо на сервак отправлять добавленный комент
      if (this.newComment.trim() !== '') {
        const newComment = this.newComment;
        this.FormPostRequest.command = 'Writing Comment';
        this.FormPostRequest.comment =this.newComment;
        this.FormPostRequest.track_id = this.$route.params.track_id;
        const data = JSON.stringify(this.FormPostRequest);
        axios.post('/MusicPage', data, {
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then((response) => {
          if(response.data.errors===''){
            console.log(response.data)
            this.track_comments.push({
              user_name: this.username,
              text_comment: newComment,
              comment_id: response.data.comment_rating_id,
              time: response.data.date
            });
          }
          else{
            console.error('Error server writing comment');
          }

        })
        .catch((error) => {
          console.error('Writing comment:', error);
        });
        this.newComment = '';
      }
    },




    removeComment(index, commentId) {
      this.FormPostRequest.command = 'Delete Comment';
      this.FormPostRequest.comment_id=commentId;
      this.FormPostRequest.track_id = this.$route.params.track_id;
      const data = JSON.stringify(this.FormPostRequest);
      axios.post('/MusicPage', data, {
        headers: {
          'Content-Type': 'application/json',
        }
      })
      .then((response) => {
        if(response.data.errors===''){
          // Здесь вы можете добавить логику для отправки удаления комментария на сервер
          console.log('Удален:', commentId);
          this.track_comments.splice(index, 1);
        }
        else{
          console.log('Errors server set rating');
        }
      })
      .catch((error) => {
        console.error('Delete Comment:', error);
      });
    },
  },
  created() {

    this.getTrackInfo();

  },

};
</script>

<style scoped>
.menu-row {
  margin-top: 0px; /* Добавленный отступ сверху */
}

.track-info {
  display: flex;
  align-items: flex-start;
  margin-top: 40px; /* Увеличенный отступ сверху */
}

.track-image {
  margin-right: 20px;
}

.track-image img {
  margin-left: 60px;
  max-width: 300px;
  height: auto;
}

.track-title {
  margin-bottom: 20px;
}

.track-meta p {
  margin: 5px 0;
}

.track-details {
  margin-left: 60px;
  font-size: 1.2rem;
}

.rating-select {
  width: 100px;
}

.rating-button {
  width: 95px;
  margin-left: 10px;
  background-color: #6d6e6d;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.rating-button:hover {
  background-color: #252625;
}

.comments-about {
  margin-left: 20px;
  margin-top: 40px;
}

.comment {
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.comment-content {
  flex-grow: 1;
  color: black;
}

.comment-actions {
  margin-left: 0px;
}
.delete-button {
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #cc0000;
}

textarea {
  margin-left: 40px;
  margin-top: 40px;
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

button {
  background-color: #6d6e6d;
  margin-left: 40px;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  margin-top: 10px;
  cursor: pointer;
}

button:hover {
  background-color: #252625;
}
</style>