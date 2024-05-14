<template>
  <div id="app">
    <MenuBar />
    <div class="back-link-container">
      <router-link to="/MainPage" class="back-link">
        <b-icon icon="arrow-left" aria-label="Previous"></b-icon>
      </router-link>
    </div>

    <div class="container">
      <h2>Изменить профиль</h2>

      <div class="form-group">
        <h4>Имя пользователя</h4>
        <p><b>Текущее имя пользователя:</b> {{ currentData[0].username }}</p>
        <div class="input-group">
          <input type="text" id="username" v-model="newUsername" class="form-control input-narrow" />
          <div class="input-group-append ml-2">
            <button class="btn btn-secondary" @click="updateUsername">Изменить</button>
          </div>
        </div>
        <small class="form-text text-muted" v-if="usernameValidationMessage">{{ usernameValidationMessage }}</small>
      </div>


      <div class="form-group">
  <h4>Email</h4>
  <p><b>Текущий email:</b> {{ currentData[0].email }}</p>
  <div class="input-group">
    <input type="email" id="email" v-model="newEmail" class="form-control input-narrow" />
    <div class="input-group-append ml-2">
      <button class="btn btn-secondary" @click="updateEmail">Изменить</button>
    </div>
  </div>
  <small class="form-text text-muted" v-if="emailValidationMessage">{{ emailValidationMessage }}</small>
</div>


      <div class="form-group mt-4">
      <h4>Пароль</h4>
<div class="input-group">
  <div class="form-group">
         <input type="password" id="password" v-model="password" class="form-control input-narrow" placeholder="Старый пароль"/>
      </div>
       <div class="form-group">
       <input type="password" id="confirmPassword" v-model="confirmPassword" class="form-control input-narrow" placeholder="Новый пароль" />
       </div>
    <div class="input-group-append ml-2">
       <button class="btn btn-secondary" @click="updatePassword">Изменить</button>
    </div>
  </div>
  <small class="form-text text-muted" v-if="passValidationMessage">{{ passValidationMessage }}</small>
</div>


      <div class="form-group mt-4 d-flex align-items-center">
        <h4 class="mr-4">Двухфакторная аутентификация</h4>
        <div class="form-check ml-auto">
          <input type="checkbox" class="form-check-input" id="second-factor" v-model="secondFactor" @change="toggleSecondFactor" />
        </div>
      </div>

     
      <div v-if="this.currentData[0].username === 'admin'" class="comment-actions">
        <div class="form-group">
  <h4>Удаление пользователя</h4>
  <div class="input-group">
    <input type="text" id="username2" v-model="userDel" class="form-control input-narrow" />
    <div class="input-group-append ml-2">
      <button class="btn btn-secondary" @click="deleteUser">Удалить</button>
    </div>
  </div>
  <small class="form-text text-muted" v-if="deleteValidationMessage">{{ deleteValidationMessage }}</small>

</div>

      </div>




      <div class="exit-button mt-4 d-flex align-items-center">
      <button class="btn btn-secondary" @click="ExitfromML">Выход</button>
    </div>


   


    </div>

    

  </div>

  
</template>



<script>
import MenuBar from '@/components/MenuBar.vue'

export default {
  name: 'ProfilePage',
  components: {
    MenuBar
  },
  data() {
    return {
      ///ДАННЫЕ С СЕРВЕРА
      currentData: [
        {
          username: 'admin',
          email: 'sasha@smth.com',
          password: '123',
          second_factor: true,
        }
      ],
    }
  },
  methods: {
    updateUsername() {
      const currentUsername = this.currentData[0].username;
      const newUsername = this.newUsername.trim();
      this.currentData[0].username='';
      ///ТУТ КАКАЯ ТО ПРОВЕРКА МОЖНО ЛИ ИЗМЕНИТЬ
      if (!newUsername) {
        this.usernameValidationMessage = 'Недопустимое имя пользователя';
        this.currentData[0].username = currentUsername;
        this.newUsername = '';
      } else if (newUsername === currentUsername) {
        this.usernameValidationMessage = 'Недопустимое имя пользователя';
        this.currentData[0].username = currentUsername;
        this.newUsername = '';
      } else if (newUsername.toLowerCase() === 'админ') {
        this.usernameValidationMessage = 'Недопустимое имя пользователя';
        this.currentData[0].username = currentUsername;
        this.newUsername = '';
      } else {
        ///ТУТ ШЛЕМ ЧТО
        this.currentData[0].username = newUsername;
        this.usernameValidationMessage = 'Изменено';
        this.newUsername = '';
      }
    },
    ///ДАЛЬШЕ АНАЛОГИЧНО
    updateEmail() {
    const currentEmail = this.currentData[0].email;
    const newEmail = this.newEmail.trim();
    this.currentData[0].email='';

    if (!newEmail) {
      this.emailValidationMessage = 'Недопустимый email';
      this.currentData[0].email = currentEmail;
      this.newEmail= '';
    } else if (newEmail === currentEmail) {
      this.emailValidationMessage = 'Недопустимый email';
      this.currentData[0].email = currentEmail;
      this.newEmail= '';
    } else {      
      this.currentData[0].email = newEmail;
      this.emailValidationMessage = 'Изменено';
      this.newEmail = ''; // Очистка поля ввода после успешного изменения
    }
    
    },
    updatePassword() {
      const currentPass = this.currentData[0].password;
      const newPass = this.confirmPassword.trim();
      const enterPass = this.password.trim();

      if (enterPass === currentPass) {
        this.passValidationMessage = 'Изменено';
        this.currentData[0].password = newPass;
        this.password = '';
        this.confirmPassword = '';
      } else {      
        this.passValidationMessage = 'Неверный пароль';
        this.password = '';
        this.confirmPassword = '';
      }
},

    toggleSecondFactor() {
      // Код для обработки изменения двухфакторной аутентификации
      console.log('Двухфакторная аутентификация:', this.secondFactor);
    },

    ExitfromML(){
      this.$router.push('/');
    },

    deleteUser(){
        const userDel = this.userDel.trim();
       console.log(userDel);
      if (userDel === 'sasha') {
        this.deleteValidationMessage = 'Пользователь удален';
        this.userDel = '';
        this.$forceUpdate();
      } else {   
        this.deleteValidationMessage = 'Пользователь не может быть удален или не существует';
        this.userDel = '';
        this.$forceUpdate(); 
      } 
         
    },


  },
  
  mounted() {
    this.secondFactor = this.currentData[0].second_factor;
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
.form-group {
  margin-bottom: 1.5rem;
}
.input-narrow {
  width: 200px; /* Установили ширину полей ввода */
}
.exit-button{
  margin-left: 50%; /* Добавили отступ слева */
}

</style>
