<template>
  <div>
    <b-card class="my-card">
      <b-aspect :aspect="2">
        <b-card class="my-card2">
          <b-aspect :aspect="11">
<!--            поле для выбора должности     -->
            <b-form-select class="select my-aspect" id="professionInput" v-model="prof">
              <b-form-select-option aria-selected="true" disabled>Выберите должность</b-form-select-option>
              <b-form-select-option v-for="profession in professions" :value="profession.name" :key="profession.id">
                {{ profession.name }}
              </b-form-select-option>
            </b-form-select>
            <b-form-input v-model="name" placeholder="Введите ФИО" class="my-aspect" id="nameInput"></b-form-input>
            <b-button variant="outline-primary" style="margin: 10px" @click="showTests">Начать тестирование</b-button>

<!--            получаем список тестов и в цикле выводим их   -->
            <div v-show="showTest" class="my-test">
              <div v-show="!end">
                <p><strong>
                  Вопрос {{ k }}/{{ len }}. {{ point.question }}
                </strong>
                </p>
                <b-form-group v-slot="{ ariaDescribedby }">
                  <b-form-radio v-model="answer" :aria-describedby="ariaDescribedby" name="some-radios"
                                value="A">
                    A. {{ point.varA }}
                  </b-form-radio>
                  <b-form-radio v-model="answer" :aria-describedby="ariaDescribedby" name="some-radios"
                                value="B">
                    B. {{ point.varB }}
                  </b-form-radio>
                  <b-form-radio v-model="answer" :aria-describedby="ariaDescribedby" name="some-radios"
                                value="C">
                    C. {{ point.varC }}
                  </b-form-radio>
                </b-form-group>
                <b-button variant="outline-primary" style="margin: 10px" @click="onNext"
                          v-show="len-1>answerList.length">
                  Далее
                </b-button>
                <div v-show="len-1===answerList.length">
                  <b-button variant="outline-primary" style="margin: 10px"
                            @click="createTest(tests[testId].profession.id)">Завершить тестирование
                  </b-button>
                </div>
              </div>
<!--              форма для отправки результатов на почту   -->
              <div v-show="end">
                <h3>Тестирование завершено!</h3>
                <b-button v-b-modal.modal-mail variant="outline-primary" style="margin: 10px">
                  Отправить результат на электронную почту
                </b-button>
                <b-modal id="modal-mail" title="Отправка результата на email" @ok="sendOnEmail">
                  <b-form-group
                    id="email"
                    label="Email"
                    label-for="email">
                    <b-form-input
                      v-model="mail"
                      id="email"
                      type="email"
                      required
                      placeholder="Введите email"
                    ></b-form-input>
                  </b-form-group>
                </b-modal>
                <b-button variant="outline-primary" style="margin: 10px" @click="mainPage">На главную
                </b-button>
              </div>
            </div>
          </b-aspect>
        </b-card>
      </b-aspect>
    </b-card>
  </div>
</template>

<script>
import Header from "./Header";
import $ from "jquery";

export default {
  name: "Tests",
  components: {Header},
  data() {
    return {
      professions: '',
      tests: '',
      prof: '',
      showTest: false,
      testId: '',
      point: '',
      answer: '',
      testList: [], // список тестов
      answerList: [], // список ответов
      professionList: [],
      len: 0, // количество вопросов в тесте
      end: false,
      result: '',
      mail: '',
      message: '',
      last: false,
      k: 1,
    }
  },
  created() {
    this.getProfession();
    this.getTests();
  },
  methods: {
    // метод срабатывает при нажатии на кнопку "начать тестирование"
    showTests() {
      const name = document.getElementById('nameInput').value;
      const profession = document.getElementById('professionInput').value;
      //   получаем количество вопросов в тесте
      this.getProfessionList()
      this.len = this.professionList.length;
      //  проверка полей имени и должности
      if ((name === '') || (profession === '')) {
        this.$bvToast.toast(`Заполните все поля`, {
          title: 'Ошибка!',
          autoHideDelay: 1000,
          appendToast: false
        })
      } else {
        //  блокируем поля, чтобы не изменялись
        $("#professionInput").prop("disabled", true);
        $("#nameInput").prop("disabled", true);
        // поинт - текущий вопрос в тесте
        this.point = this.tests[this.testId];
        // в цикле ищем вопросы для конкретной должности
        for (let i = 0; i < this.tests.length - 1; i++) {
          if (this.point.profession.name === profession) {
            this.showTest = true;
            break
          } else {
            this.testId++;
            this.point = this.tests[this.testId];
          }
        }
      }
    },
    getProfessionList() {
      for (let i = 0; i < this.tests.length; i++) {
        if (this.prof === this.tests[i].profession.name) {
          this.professionList.push(this.tests[i].id)
        }
      }
    },
    // при нажатии на кнопку Далее
    onNext() {
      // к - счетчик вопросов
      this.k++;
      // проверяем что ответ не пустой
      if (this.answer !== "") {
        //  создаем список с ответами и пройденными тестами
        this.createList(this.point.id, this.answer)
        while (true) {
          this.testId++;
          this.point = this.tests[this.testId];
          if (this.point.profession.name === this.prof) {
            this.answer = "";
            break
          }
        }
      } else {
        this.$bvToast.toast(`Выберите вариант ответа`, {
          title: 'Ошибка!',
          autoHideDelay: 1000,
          appendToast: false
        })
      }
    },
    createList(id, answer) {
      this.testList.push(id);
      this.answerList.push(answer)
    },
    // сохранение тестирования
    createTest(id) {
      if (this.answer !== "") {
        this.createList(this.point.id, this.answer);
        this.getResult();
        $.ajax({
          url: "http://127.0.0.1:8000/answer/create/",
          type: "POST",
          data: {
            name: this.name,
            profession: id,
            test: this.testList.join(),
            answer: this.answerList.join(),
            result: this.result,
          },
          success: (response) => {
            this.end = true;
          },
          error: (response) => {
            alert("Произошла непредвиденная ошибка");
            console.log(response)
          }
        })
      } else {
        this.$bvToast.toast(`Выберите вариант ответа`, {
          title: 'Ошибка!',
          autoHideDelay: 1000,
          appendToast: false
        })
      }
    },
    // отправка результата на почту
    sendOnEmail() {
      $.ajax({
        url: "http://127.0.0.1:8000/mail/",
        type: "POST",
        data: {
          mail: this.mail,
          message: "Поздравляем, " + this.name + "! Вы прошли тестирование. Ваш результат: " + this.result,
        },
        success: (response) => {
          alert('Письмо отправлено. Проверьте свою электронную почту.')
          console.log()
        },
        error: (response) => {
          alert("Письмо не отправлено. Проверьте правильность введенных данных");
          console.log(response)
        }
      })
    },
    // счетчик правильных ответов
    getResult() {
      let number = 0;
      let j = 0;
      for (let i = 0; i < this.tests.length; i++) {
        if (this.tests[i].id == this.testList[j]) {
          if (this.tests[i].correct_answer === this.answerList[j]) {
            number++;
          }
          j++;
        }
      }
      this.result = number + '/' + this.testList.length
    }
    ,
    mainPage() {
      this.$router.push({name: "mainPage"})
    },
    getProfession() {
      $.ajax({
        url: "http://127.0.0.1:8000/profession/all/",
        methods: 'GET',
        success: (response) => {
          this.professions = response;
        },
      });
    }
    ,
    getTests() {
      $.ajax({
        url: "http://127.0.0.1:8000/test/all/",
        methods: 'GET',
        success: (response) => {
          this.tests = response;
          this.testId = 0;
          console.log(response)
        },
        error: (response) => {
          alert("Невозможно загрузить список тестов. Проверьте подключение к интернету!");
          console.log(response)
        }
      });
    }
    ,
  }
}
</script>

<style scoped>
.my-aspect {
  width: 450px;
  margin: 10px;
  float: left;
}

.my-test {
  text-align: left;
  margin: 15px;
  margin-top: 50px;
}
</style>
