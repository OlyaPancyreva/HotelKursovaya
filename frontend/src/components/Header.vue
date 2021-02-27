<template>
  <div>
<!--    шапка сайта   -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Hotel</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="openMainPage">Главная <span class="sr-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">О нас <span class="sr-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Номера <span class="sr-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Услуги <span class="sr-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Контакты <span class="sr-only"></span></a>
          </li>
        </ul>
      </div>
      <div>
        <a class="btn my-0 mr-md-auto text-info" href="#" v-show="get_auth" @click="openTests">Пройти тестирование</a>
        <a class="btn my-0 mr-md-auto text-info" href="#" v-if="isAdmin == 'admin'" @click="openResult">Результаты тестирования</a>
        <a v-b-modal.modal-2 class="btn p-3 text-dark" href="#" v-show="!get_auth">Регистрация</a>
        <a v-b-modal.modal-1 class="btn btn-outline-primary" href="#" v-show="!get_auth">Вход</a>
        <a class="btn btn-outline-primary" v-show="get_auth" @click="logout">Выйти</a>
      </div>
      <!--    модальное окно для авторизации    -->
      <b-modal id="modal-1" title="Авторизация" @ok="auth">
        <b-form-group
          id="login"
          label="Логин"
          label-for="login"
        >
          <b-form-input
            v-model="login"
            id="login"
            type="email"
            required
            placeholder="Введите логин"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="password"
          label="Пароль"
          label-for="password"
        >
          <b-form-input
            v-model="password"
            id="password"
            type="password"
            required
            placeholder="Введите пароль"
          ></b-form-input>
        </b-form-group>
      </b-modal>
      <!--    модальное окно для регистрации  -->
      <b-modal id="modal-2" title="Регистрация" @ok="registration">
        <b-form-group
          id="login-reg"
          label="Логин"
          label-for="login-reg"
          description="Только буквы, цифры и символы @/./+/-/_"
        >
          <b-form-input
            v-model="login_reg"
            id="login-reg"
            type="text"
            required
            placeholder="Введите логин"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="email-reg"
          label="Email"
          label-for="email-reg">
          <b-form-input
            v-model="email_reg"
            id="email-reg"
            type="email"
            required
            placeholder="Введите email"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="password-reg"
          label="Пароль"
          label-for="password-reg"
          description="Пароль должен содержать не менее 8 символов"
        >
          <b-form-input
            v-model="password_reg"
            id="password-reg"
            type="password"
            required
            placeholder="Введите пароль"
          ></b-form-input>
        </b-form-group>
      </b-modal>
    </nav>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Header",
    data() {
      return {
        login: '',
        password: '',
        login_reg: '',
        password_reg: '',
        email_reg: '',
        get_auth: '',
        isAdmin: '',
      }
    },
    methods: {
      openTests() {
        this.$router.push({name: "tests"});
      },
      openResult(){
        this.$router.push({name: "resultPage"});
      },
      /*  авторизация   */
      auth(bvModalEvt) {
        $.ajax({
          url: "http://127.0.0.1:8000/auth/token/login/",
          type: "POST",
          data: {
            username: this.login,
            password: this.password
          },
          success: (response) => {
            sessionStorage.setItem("auth_token", response.auth_token);
            sessionStorage.setItem("username", this.login);
            this.isAdmin = this.login;
            this.get_auth = true;
          },
          error: (response) => {
            if (response.status === 400) {
              alert("Неверный логин или пароль");
            }
            console.log(response)
          }
        })
      },
      /*  регистрация */
      registration(bvModalEvt) {
        $.ajax({
          url: "http://127.0.0.1:8000/auth/users/",
          type: "POST",
          data: {
            username: this.login_reg,
            password: this.password_reg,
            email: this.email_reg,
          },
          success: (response) => {
            alert("Вы успешно зарегистрировались")
          },
          error: (response) => {
            if (response.status === 400) {
              alert("Неверно заполнены поля");
            }
            console.log(response)
          }
        })
      },
      /*  проверка авторизации  */
      check_auth() {
        this.get_auth = sessionStorage.getItem("auth_token") !== null;
        this.isAdmin = sessionStorage.getItem('username');
      },
      /*  выход */
      logout() {
        this.get_auth = false;
        sessionStorage.removeItem("auth_token");
        sessionStorage.removeItem("username");
        this.isAdmin = '';
        this.openMainPage();
      },
      openMainPage() {
        this.$router.push({name: "mainPage"})
      },
    },
    created() {
      this.check_auth()
    }
  }
</script>

<style scoped>
  .btn {
    margin-left: 10px;
    margin-right: 10px;
  }
</style>
