<template>
  <h1>Home page</h1>
  <div
    class="score"
    v-for="scoreEntry in registeredScores"
    v-bind:key="scoreEntry.date"
  >
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    const Quizinfo = await quizApiService.getQuizInfo();
    this.registeredScores = Quizinfo.data.scores;
  },
};
</script>

<style>
html {
  padding: 25;
  margin: 25;
  font-family: Roboto, Arial, sans-serif;
  font-size: 28px;
  color: #666;
}

h1 {
  color: #1db623;
}

a {
  padding: 8px;
  margin-bottom: 10px;
  outline: none;
  color: #1c87c9;
  cursor: pointer;
}

.score {
  font-weight: bold;
  color: white;
}
</style>