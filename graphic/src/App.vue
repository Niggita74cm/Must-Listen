<template>
  <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
    <div class="row" style="width: 20%;">
        <div class="col-xl-16">
          <form @submit.prevent="LoginUser" novalidate>

            <div v-show="type_list === 1 && main_page === 0" class="login">
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
                    <input v-model="formRegisr.passwrd" type="password" class="form-control" id="passwrd">
                    <button @click="togglePasswordVisibility('passwrd')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                  </div>
                </div>


                <div class="mb-3">
                <label for="passwrd_only" class="form-label">Одноразовый пароль</label>
                  <div class="input-group">
                    <input v-model="formRegisr.passwrd_only" type="password" class="form-control" id="passwrd_only">
                    <button @click="togglePasswordVisibility('passwrd_only')" type="button" class="btn btn-outline-secondary btn-sm" >Показать пароль</button>
                  </div>
                </div>


              <button  @click="go_to_main" type="button" class="btn btn-dark d-block mt-3">Войти</button>

              <button @click="change_list" type="button" class="btn btn-light btn-sm d-block mt-3">Регистрация</button>
            </div>




          </form>
          <form @submit.prevent="RegisterUser" novalidate>
            <div v-show="type_list === 2 && qr_step === 4" class="registry">
              <div class="mb-3 login">
                 <h2>Регистрация</h2>
               </div>

                <div class="mb-3">
                 <label for="name" class="form-label">Имя</label>
                 <input v-model="formRegisr.name" type="text" class="form-control" id="name" >
               </div>

               <div class="mb-3">
                 <label for="surname" class="form-label">Фамилия</label>
                 <input v-model="formRegisr.surname" type="text" class="form-control" id="surname">
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
               <button @click="qr_code" type="submit" class="btn btn-dark d-block mt-3">Зарегистрироваться</button>
               <button @click="back_list" type="button" class="btn btn-light btn-sm d-block mt-3">Назад</button>

            </div>            
          </form>



          <form @submit.prevent="QR_list" novalidate>

              <div v-show="qr_step === 5" class="login_second">
                <div class="mb-3 login">
                  <h2>Отсканируйте QR-код</h2>
                </div>
                <div class="text-center">
                  <img src="./qr.jpg" class="rounded" alt="...">
                </div>


                <button @click="qr_code_back" type="button" class="btn btn-light btn-sm d-block mt-3">Назад</button>
                <!-- Тут надо как то отловить сканирование QR и вызвать go_to_main()-->
              </div>
          </form>
           


          <div v-show="main_page === 1">
            
            <h2>Главная страница</h2>
            <button  @click="go_to_auth" type="button" class="btn btn-dark d-block mt-3">Выйти</button>
          </div>


        </div>
    </div>
  </div>
</template>

<script>


export default {
    data(){
      return {
        type_list: 1,
        qr_step:4,
        main_page: 0,
        formLogin: {
          login: '',
          passwrd: '',
          passwrd_only: ''
        },
        formRegisr: {
          name: '',
          surname: '',
          emale: '',
          username: '',
          pass: '',
          confirm_pass: ''
        }
      }
    },
    methods: {
      change_list(){
        this.type_list++
      },

      togglePasswordVisibility(inputId) {
        let passInput = document.getElementById(inputId);
        if (passInput.type === "password") {
          passInput.type = "text";
        } else {
          passInput.type = "password";
        }
      },


      back_list(){
        this.type_list--
      },

      RegisterUser(){
        console.log('Регистрация прошла успешно'),
        console.log(this.formRegisr.name)
      },

      LoginUser(){
        console.log('Попытка входа')
      },

      qr_code(){
        this.qr_step++
      },
      qr_code_back(){
        this.qr_step--
      },
      go_to_main(){
        this.main_page++
      },
      go_to_auth(){
        this.main_page--
      }

    }
}
</script>

<style>

</style>
