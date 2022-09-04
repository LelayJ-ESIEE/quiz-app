<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
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
      registeredScores: []
    };
  },
  async created() {
		console.log("Composant Home page 'created'");
    const info = await quizApiService.getQuizInfo();
    this.registeredScores = info.data.scores;
  }
};
</script>

<style>
h1 {
  color: #198754;
}
</style>