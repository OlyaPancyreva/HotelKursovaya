<template>
  <div>
    <b-card class="my-card">
      <b-aspect :aspect="2">
        <b-card class="my-card3">
          <b-aspect :aspect="11">

            <table class="table table-hover" v-show="table">
              <thead>
              <tr>
                <th scope="col">ФИО</th>
                <th scope="col">Должность</th>
                <th scope="col">Результат</th>
                <th scope="col"></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="result in results">
                <td>{{ result.name }}</td>
                <td> {{ result.profession.name }}</td>
                <td> {{ result.result }}</td>
                <td>
                  <a v-b-modal.modal class="btn btn-outline-primary" href="#" @click="showDetail(result.id)">
                    подробнее
                  </a>
                </td>
              </tr>
              </tbody>
            </table>

            <b-modal id="modal" title="Просмотр детальной информации">
              <h4>
                ФИО: {{ point.name }}
              </h4>
              <h4>
                Должность: {{ profession }}
              </h4>
              <h6>Ответы:</h6>
              <div v-for="i in answerList.length">
                <h6 v-if="answerList[i-1] === resultList[i-1]" style="color: green">
                  {{ i }}. {{ answerList[i - 1] }}
                </h6>
                <h6 v-else style="color: red">
                  {{ i }}. {{ answerList[i - 1] }}
                </h6>
              </div>
            </b-modal>
          </b-aspect>
        </b-card>
      </b-aspect>
    </b-card>
  </div>
</template>

<script>
import Header from "./Header";
import $ from 'jquery'

export default {
  name: "ResultPage",
  components: {Header},
  data() {
    return {
      results: '',
      point: '',
      table: true,
      detail: false,
      tests: '',
      testList: '',
      answerList: '',
      resultList: [],
      profession: '',
    }
  },
  created() {
    this.uploadResults();
    this.uploadTests();
  },
  methods: {
    uploadTests() {
      $.ajax({
        url: "http://127.0.0.1:8000/test/all/",
        methods: 'GET',
        success: (response) => {
          this.tests = response;
        },
        error: (response) => {
          alert("Невозможно загрузить список тестов. Проверьте подключение к интернету!");
          console.log(response)
        }
      });
    },
    uploadResults() {
      $.ajax({
        url: "http://127.0.0.1:8000/answer/all/",
        methods: 'GET',
        success: (response) => {
          this.results = response;
        },
        error: (response) => {
          alert("ERROR");
          console.log(response)
        }
      });
    },
    showDetail(id) {
      this.resultList = [];
      for (let i = 0; i < this.results.length; i++) {
        if (this.results[i].id === id) {
          this.point = this.results[i]
          this.testList = this.results[i].test
          this.answerList = this.results[i].answer
          this.profession = this.results[i].profession.name
        }
      }
      this.testList = this.testList.split(',')
      this.answerList = this.answerList.split(',')
      let j = 0;
      for (let i = 0; i < this.tests.length; i++) {
        console.log(this.testList[j])
        console.log(this.tests[i])
        if (this.tests[i].id == this.testList[j]) {
          this.resultList.push(this.tests[i].correct_answer)
          j++;
        }
      }
      console.log(this.resultList)
    },
  }
}
</script>

<style scoped>
.my-card3 {
  max-width: 1500px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}

.res {
  margin: 20px;

}
</style>
