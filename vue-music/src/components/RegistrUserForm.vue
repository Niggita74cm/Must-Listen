<template>
    <div class="d-flex justify-content-center align-items-center" style="height: 87vh;">
      <div class="row" style="width: 80%;">
          <div class="col-xl-16">
            <form @submit.prevent="RegisterUser" novalidate>
              <div class="registry">
                <div class="mb-3 login">
                   <h2>Регистрация</h2>
                 </div>
  
                  
                 <div class="mb-3">
                   <label for="email" class="form-label">Электронная почта</label>
                   <input v-model="formRegisr.email" type="text" class="form-control" id="email">
                 </div>
  
                 <div class="mb-3">
                   <label for="username" class="form-label">Имя пользователя</label>
                   <input v-model="formRegisr.username" type="text" class="form-control" id="username">
                 </div>
  
                 <div class="mb-3">
                  <label for="pass" class="form-label">Пароль</label>
                    <div class="input-group">
                      <input v-model="formRegisr.password" type="password" class="form-control" id="pass">
                      <button @click="togglePasswordVisibility('pass')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>
  
                 <div class="mb-3">
                  <label for="confirm_pass" class="form-label">Подтверждение пароля</label>
                    <div class="input-group">
                      <input v-model="formRegisr.confirmPassword" type="password" class="form-control" id="confirm_pass">
                      <button @click="togglePasswordVisibility('confirm_pass')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>


                  <div class="d-flex flex-column align-items-start">
                    <button type="submit" class="btn btn-dark btn-md mb-2">Зарегистрироваться</button>
                    <router-link to="/" class="btn btn-light btn-md">Назад</router-link>
                    </div>


  
              </div>            
            </form>         
    
          </div>
      </div>
    </div>
  </template>
  
  <script>
  

  import axios from "axios";
  export default {
    name: '_registration',
      data(){
        return {
          formRegisr: {
            email: '',
            username: '',
            password: '',
            confirmPassword: ''
          }
        }
      },
      methods: {
        togglePasswordVisibility(inputId) {
          let passInput = document.getElementById(inputId);
          if (passInput.type === "password") {
            passInput.type = "text";
          } else {
            passInput.type = "password";
          }
        },
        RegisterUser() {
          const data = JSON.stringify(this.formRegisr);
          axios.post('/api/RegistrUserPage', data, {
            headers: {
              'Content-Type': 'application/json',
            }
          })
          .then((response) => {
            if (response.data === ''){
              this.$router.push('/MainPage');
            }
            else{
              //ЗДЕСЬ ОБРАБОТКА ОШИБОК ДОПУЩЕННЫХ ПОЛЬЗОВАТЕЛЕМ ПРИ
              // РЕГИСТРАЦИИ С БЕКА ПРИХОДИТ В response.data
              console.log(response.email);
            }

          })
          .catch((error) => {
            console.error('Error during registration:', error);
            this.$router.push('/MainPage');
          });
        },
      },
  }
  </script>
  
  <style>
  
  </style>
  