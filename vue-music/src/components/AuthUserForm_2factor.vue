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
                  <label for="passwrd_only" class="form-label">Одноразовый пароль</label>
                    <div class="input-group">
                      <input v-model="formLogin.code" type="password" class="form-control" id="passwrd_only">
                      <button @click="togglePasswordVisibility('passwrd_only')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>
                  
                  <button class="btn btn-dark d-block mt-3" @click="IsLogin" type="button">Войти</button>                  
                  <div v-if="!isLoginSuccessful" class="mt-3 text-danger">Неверный одноразовый пароль</div>
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
          isLoginSuccessful: false,
          formLogin: {
            code: ''
          },
        }
      },
      methods: {
        SendOneTimePassword(){
          axios.get('/api/2factor')
          .then((res) => {
            console.log("One-time password has been sent")
            console.log(res)
          })
          .catch((error) => {
            console.error(error);
          });
        },
        IsLogin() {

          const DataFromPost = JSON.stringify(this.formLogin);
          axios.post('/api/2factor', DataFromPost, {
            headers: {
              'Content-Type': 'application/json',
            }
          })
          .then((response) => {
            this.isLoginSuccessful = response.data.isLoginSuccessful;
            this.$router.push('/MainPage');
          })
          .catch((error) => {
            console.error('Authentication error:', error);
          });
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
      created() {
        this.SendOneTimePassword();
      }
  }
  </script>
  
  <style>
  
  </style>
  