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
                   <label for="emale" class="form-label">Электронная почта</label>
                   <input v-model="formRegisr.emale" type="text" class="form-control" id="emale">
                 </div>
  
                 <div class="mb-3">
                   <label for="username" class="form-label">Имя пользователя</label>
                   <input v-model="formRegisr.username" type="text" class="form-control" id="username">
                 </div>
  
                 <div class="mb-3">
                  <label for="pass" class="form-label">Пароль</label>
                    <div class="input-group">
                      <input v-model="formRegisr.pass" type="password" class="form-control" id="pass">
                      <button @click="togglePasswordVisibility('pass')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>
  
                 <div class="mb-3">
                  <label for="confirm_pass" class="form-label">Подтверждение пароля</label>
                    <div class="input-group">
                      <input v-model="formRegisr.confirm_pass" type="password" class="form-control" id="confirm_pass">
                      <button @click="togglePasswordVisibility('confirm_pass')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                    </div>
                  </div>


                  <div class="d-flex flex-column align-items-start">
                    <router-link to="/MainPage" class="btn btn-dark btn-md mb-2">Зарегистрироваться</router-link>
                    <router-link to="/" class="btn btn-light btn-md">Назад</router-link>
                    </div>


  
              </div>            
            </form>         
    
          </div>
      </div>
    </div>
  </template>
  
  <script>
  

  export default {
    name: '_registration',
      data(){
        return {
          formRegisr: {
            emale: '',
            username: '',
            pass: '',
            confirm_pass: ''
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
  
        RegisterUser(){
          console.log('Регистрация прошла успешно'),
          console.log(this.formRegisr.name)
        },
         
    }
  }
  </script>
  
  <style>
  
  </style>
  