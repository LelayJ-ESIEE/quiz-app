import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutView from '../views/AboutView.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ResultScorePage from '../views/ResultScorePage.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/about",
      name: "AboutView",
      component: AboutView,
    },
    {
      path: "/start-new-quiz-page",
      name: "NewQuizPage",
      component: NewQuizPage,
    },
    {
      path: "/questions",
      name: "QuestionsManager",
      component: QuestionsManager,
    },
    {
      path: "/result-score-page",
      name: "ResultScorePage",
      component: ResultScorePage,
    },
    // ... autres routes
  ]
})

export default router
