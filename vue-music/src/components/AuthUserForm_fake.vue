<template>
    <div class="d-flex justify-content-center align-items-center" style="height: 80vh;">
      <div class="row" style="width: 100%;">
          <div class="col-xl-16">
            <form @submit.prevent="LoginUser" novalidate>

              <div class="login">
                <div class="mb-3 login">
                  <h2>Вход в систему</h2>
                </div>

                <div class="mb-3">
                  <label for="login" class="form-label">Логин</label>
                  <input v-model="formLogin.login" type="text" class="form-control" id="login" >
                </div>


                <div class="mb-3">
                  <label for="passwrd" class="form-label">Пароль</label>
                    <div class="input-group">
                      <input v-model="formLogin.password" type="password" class="form-control" id="passwrd">
                      <button @click="togglePasswordVisibility('passwrd')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>



                  <button class="btn btn-dark d-block mt-3" @click="IsLogin" type="button">Войти</button>
                  <div v-if="!isLoginSuccessful" class="mt-3 text-danger">Неверный логин или пароль</div>


                  <p class="mt-3">Ещё не зарегистрированы? <router-link to="/RegistrUserPage">Регистрация</router-link></p>
              </div>
            </form>
          </div>
      </div>
    </div>
  </template>

  <script>


  import axios from "axios";

  export default {
    name: 'authentication_registration',
      data(){
        return {
          isLoginSuccessful: true,
          formResponse:{
            second_factor: false,
            access_user: false
          },
          formLogin: {
            login: '',
            password: ''
          },
        }
      },
      methods: {
        IsLogin() {
          const data = JSON.stringify(this.formLogin);
          axios.post('/api/fauth/', data, {
            headers: {
              'Content-Type': 'application/json',
            }
          })
          .then((response) => {
            if(response.data.access_user===true){
              this.$router.push('/');
            }
            else {
              this.$router.push('/');
            }
          })
          .catch((error) => {
            console.error('Authentication error:', error);
          });
          ///ТУТ ВМЕСТО ЭТОЙ ПРОВЕРКИ НАДО ОТПРАВЛЯТЬ НА СЕРВЕР ДАННЫЕ И ДЕЛАТЬ ПРОВЕРКУ
          // if (this.formLogin.login === 'admin' && this.formLogin.passwrd === '123') {
          //   // this.isLoginSuccessful = true;
          //   if (this.second_factor==false){
          //     this.$router.push('/MainPage');
          //   }
          //   else {
          //     this.$router.push('/2factor');
          //   }
          // }
          // else {
            // this.isLoginSuccessful = false;
          // }
        },

        resetForm() {
        this.formLogin.login = '';
        this.formRegisr.passwrd = '';
        },

        togglePasswordVisibility(inputId) {
          let passInput = document.getElementById(inputId);
          if (passInput.type === "password") {
            passInput.type = "text";
          } else {
            passInput.type = "password";
          }
        },

        LoginUser(){
          console.log('Попытка входа')
        },

      },
  }
  </script>

  <style>

  </style>