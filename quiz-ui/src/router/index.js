import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutView from '../views/AboutView.vue'
import NewQuizPage from '../views/NewQuizPage.vue'

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
    // ... autres routes
  ]
})

export default router
