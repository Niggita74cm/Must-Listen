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
            <h2>{{ Musicinfo[0].track_name }}</h2>
          </div>
          <div class="track-meta">
            <p><b>Альбом</b> {{ Musicinfo[0].album_name }}</p>
            <p><b>Исполнитель</b> {{ Musicinfo[0].artists }}</p>
            <p><b>Рейтинг</b> {{ Musicinfo[0].popurarity }}</p>
            <p><b>Продолжительность</b> {{ formatDuration(Musicinfo[0].duratind_ms) }}</p>
            <p>
              <b>Поставить оценку</b>
              <select v-model="rating1" class="rating-select">
                <option v-for="rating in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :value="rating" :key="rating">{{ rating }}</option>
              </select>
              <button @click="submitRating" class="rating-button">Оценить</button>
            </p>
            <p v-if="userRating">Ваша оценка {{ userRating }}</p>
          </div>
        </div>

        <div class="comment-form">
        <textarea v-model="newComment" placeholder="Введите комментарий" rows="3"></textarea>
        <button @click="addComment">Комментировать</button>
      </div>
   



      </div>
      <div class="comments-about">
        <h3>Комментарии</h3>
        <div v-for="(comment, index) in Comments" :key="index" class="comment">
          
          <div class="comment-content">
          <p><strong>{{ comment.user_name }}</strong><br/> {{ comment.text_connent }}</p>
        </div>
        <div v-if="current_user === 'admin'" class="comment-actions">
            <button @click="removeComment(index,comment.comment_id)" class="delete-button">Удалить</button>
          </div>

          <button
            v-if="comment.user_name === current_user"
            @click="removeComment(index, comment.comment_id)"
            class="delete-button"
          >
            Удалить
          </button>

          <hr v-if="index !== Comments.length - 1">
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import MenuBarAuth from './MenuBarAuth.vue';
  
  export default {
    name: 'MusicPage',
    components: {
      MenuBarAuth,
    },
    computed: {
      musicId() {
        return this.$route.params.id; ///ЭТО ID ТРЕКА ПО КОТОРОМУ КЛИКНУЛИ
      },
    },
    data() {
      return {
        userRating: null, ///ЕСЛИ ПОСТАВЛЕНА ТО ПЕРЕДАТЬ СЮДА
        rating1: null,
        current_user: 'sasha', //ЕСЛИ admin БУДЕТ КНОПКА УДАЛИТЬ
        ///ДАННЫЕ О ТРЕКЕ ТОЖЕ НУЖНЫ С СЕРВЕРА
        Musicinfo: [
          {
            track_id: 1,
            track_name: 'Wolves',
            album_name: 'The Life Of Pablo',
            artists: 'Kanye West',
            popurarity: 5,
            duratind_ms: 249458,
          },
        ],
        //КАРТИНОЧКА С СЕРВЕРА
        images: [
          { id: 1, url: 'https://avatars.yandex.net/get-music-content/41288/5c92aeb1.a.3555472-1/m1000x1000', alt: 'Image 1', link: 'https://music.yandex.ru/album/3555472' },
        ],
        //КОММЕНТАРИИ С СЕРВЕРА
        Comments: [
        {
            comment_id: 1,
            user_name: 'sasha0021',
            text_connent: '👍',
        },
        {
            comment_id: 2,
            user_name: 'user',
            text_connent: 'Best ❤️',
        },
        {
            comment_id: 3,
            user_name: 'star15',
            text_connent: 'I dont like it(((',
        },
        {
            comment_id: 4,
            user_name: 'lover_',
            text_connent: 'Listen every day',
        },
        {
            comment_id: 5,
            user_name: 'music_user',
            text_connent: 'This is my favourite track!!!😍😍😍',
        },
      ],
    };
  },
  methods: {
    formatDuration(durationMs) {
      const minutes = Math.floor(durationMs / 60000);
      const seconds = Math.floor((durationMs % 60000) / 1000);
      return `${minutes}:${seconds.toString().padStart(2, '0')}`;
    },

    submitRating() {
      this.userRating = this.rating1;
      // Здесь вы можете добавить логику для отправки рейтинга на сервер
      console.log('Оценка:', this.userRating);
    },
    removeComment(index, commentId) {
    // Здесь вы можете добавить логику для отправки удаления комментария на сервер
      console.log('Удален:', commentId);
      this.Comments.splice(index, 1);
    },
    addComment() {
    //Здесь надо на сервак отправлять добавленный комент
      if (this.newComment.trim() !== '') {
        const newCommentId = this.Comments.length + 1;
        this.Comments.push({
          user_name: this.current_user,
          text_connent: this.newComment,
          comment_id: newCommentId,
        });
        console.log('Добавлен комент:');
        this.newComment = '';
      }
    },
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
  