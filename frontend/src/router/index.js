import Vue from 'vue'
import Router from 'vue-router'
import MainPage from "../components/MainPage";
import Tests from "../components/Tests";
import ResultPage from "../components/ResultPage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'mainPage',
      component: MainPage,
    },
    {
      path: '/test',
      name: 'tests',
      component: Tests,
    },
    {
      path: '/all',
      name: 'resultPage',
      component: ResultPage,
    }
  ]
})
