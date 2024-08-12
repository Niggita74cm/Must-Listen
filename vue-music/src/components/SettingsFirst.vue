<!--ВОЗМОЖНО СТОИТ ДОБАВИТЬ УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЕМ СВОЕГО АККАУНТА-->
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
        <p><b>Текущее имя пользователя:</b> {{ UserInfo.username }}</p>
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
  <p><b>Текущий email:</b> {{ UserInfo.email }}</p>
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

     
  <div v-if="this.UserInfo.NumberPrivileges === 'admin'" class="comment-actions">
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


    <div class="form-group">
      <h4>Добавление треков:</h4>
      <div class="input-group">
        <input type="text" id="namedatabase" v-model="BDTracks" class="form-control input-narrow" />
        <div class="input-group-append ml-2">
          <button class="btn btn-secondary" @click="AddTracks">Добавить</button>
        </div>
      </div>
      <small class="form-text text-muted" v-if="AddTracksValidationMessage">{{ AddTracksValidationMessage }}</small>
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
import axios from "axios";
export default {
  name: 'ProfilePage',
  components: {
    MenuBar
  },
  data() {
    return {
      UserInfo:{
          username: '',
          email: '',
          second_factor: false,
          NumberPrivileges: ''
      },
      ConfigurationOptions:{
        SettingsCommand: '',
        NewData: '',
        OldData: ''
      },
      SettingsPostResponse:{
            ResultCommand: false,
            Message: ''
      }
    }
  },
  methods: {
    getUserInfo(){
      axios.get('/SettingsF')
          .then((res) => {
            this.UserInfo.email = res.data.email;
            this.UserInfo.username = res.data.username;
            this.UserInfo.NumberPrivileges = res.data.NumberPrivileges;
            this.UserInfo.second_factor = res.data.second_factor;
            //this.secondFactor = this.UserInfo.second_factor;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    PostUpdateRequest(NewData, Command, OldData){
      this.ConfigurationOptions.SettingsCommand = Command
      this.ConfigurationOptions.NewData = NewData
      this.ConfigurationOptions.OldData = OldData
      const DataFromPost = JSON.stringify(this.ConfigurationOptions);
          axios.post('/SettingsF', DataFromPost, {
            headers: {
              'Content-Type': 'application/json',
            }
          })
          .then((response) => {
            this.SettingsPostResponse.Message=response.data.Message;
            this.SettingsPostResponse.ResultCommand = response.data.ResultCommand;
          })
          .catch((error) => {
            console.error('Authentication error:', error);
          });
    },
    updateUsername() {
      const newUsername = this.newUsername.trim();
      this.PostUpdateRequest(newUsername, 'UpdateUsername',  '');
      if (this.SettingsPostResponse.ResultCommand===true){
        this.UserInfo.username = newUsername;
        this.usernameValidationMessage = 'Логин изменен';
      }
      else {
        this.usernameValidationMessage = this.SettingsPostResponse.Message;
      }
      this.newUsername = '';
    },
    updateEmail() {
      const newEmail = this.newEmail.trim();
      this.PostUpdateRequest(newEmail, 'UpdateEmail',  '');
      if (this.SettingsPostResponse.ResultCommand===true){
        this.UserInfo.email = newEmail;
        this.emailValidationMessage = 'Электронная почта изменена';
      }
      else {
        this.emailValidationMessage = this.SettingsPostResponse.Message;
      }
      this.newEmail = '';
    },
    updatePassword() {
      const newPass = this.confirmPassword.trim();
      const currentPass = this.password;
      this.PostUpdateRequest(newPass, 'UpdatePassword', currentPass);
      if (this.SettingsPostResponse.ResultCommand===true){
        this.passValidationMessage = 'Пароль изменен';
      }
      else {
        this.passValidationMessage = this.SettingsPostResponse.Message;
      }
      this.confirmPassword = '';
      this.password = '';
    },
    toggleSecondFactor() {
      const newSecondFactor = this.secondFactor;
      this.PostUpdateRequest(String(newSecondFactor), 'UpdateSecondFactor', '');
      if (this.SettingsPostResponse.ResultCommand===true) {
        this.UserInfo.second_factor = newSecondFactor;
      }
    },
    ExitfromML(){
      this.PostUpdateRequest('', 'LogOutAccount', '');
      this.$router.push('/');
    },


    DeleteYourSelf(){
      //ДОБАВИТЬ ВО ФРОНТЕ
      this.PostUpdateRequest('', 'DeleteYourself', '');
      this.$router.push('/');
    },
    deleteUser(){
      const userDel = this.userDel.trim();
      this.PostUpdateRequest(userDel, 'DeleteUser', '');
      if (this.SettingsPostResponse.ResultCommand===true) {
        this.deleteValidationMessage = 'Пользователь удален';
      }
      else{
        this.deleteValidationMessage = this.SettingsPostResponse.Message;
      }
      this.userDel = '';
    },
    deleteComment(){

    },

    AddTracks(){
      const NameDatabaseTracks = this.BDTracks.trim();
      this.PostUpdateRequest(NameDatabaseTracks, 'AddTracks', '');
      if (this.SettingsPostResponse.ResultCommand===true) {
        this.AddTracksValidationMessage = 'Треки добавлены';
      }
      else{
        this.AddTracksValidationMessage = this.SettingsPostResponse.Message;
      }
      this.userDel = '';
    }

  },
  created() {
        this.getUserInfo();
        this.secondFactor = this.UserInfo.second_factor;
  },
  mounted() {
    this.secondFactor = this.UserInfo.second_factor;
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
