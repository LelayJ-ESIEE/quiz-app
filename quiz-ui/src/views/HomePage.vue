<template>
  <h1>Home page</h1>
  <div
    class="score"
    v-for="scoreEntry in registeredScores"
    v-bind:key="scoreEntry.date"
  >
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <br />
  <router-link id="demarrer" to="/start-new-quiz-page" class="btn btn-primary"
    >Démarrer le quiz !</router-link
  >
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
}

h1 {
  color: hsla(160, 100%, 37%, 1);
}

#demarrer {
  margin: 3em 10em 0em 0em;
}

.score {
  font-weight: bold;
  color: white;
}
</style>