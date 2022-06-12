<template>
  <h1>
    Votre score {{ playerName }} est de : {{ currentScore }} /
    {{ totalNumberOfQuestion }}
  </h1>
  <br />
  <div
    class="score"
    v-for="scoreEntry in registeredScores"
    v-bind:key="scoreEntry.date"
  >
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/" class="btn btn-primary" id="accueil"
    >Retour à la page d'accueil</router-link
  >
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "ResultScorePage",
  data() {
    return {
      currentScore: 0,
      totalNumberOfQuestion: 0,
      playerName: "",
      registeredScores: [],
    };
  },
  async created() {
    const quizInfo = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = quizInfo.data.size;
    this.currentScore = participationStorageService.getParticipationScore();
    this.playerName = participationStorageService.getPlayerName();
    this.registeredScores = quizInfo.data.scores;
  },
};
</script>

<style>
.score {
  font-weight: bold;
  color: white;
}

#accueil {
  margin: 3em 10em 0em 0em;
}
</style>