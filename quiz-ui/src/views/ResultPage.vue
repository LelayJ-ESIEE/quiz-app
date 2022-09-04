<template>
	<h1>Résultats</h1>
	{{ playerName }}, votre score est de {{ participationScore }}/{{ totalNumberOfQuestion }}.

	<h2>Classement</h2>
	<div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
		{{ scoreEntry.playerName }} - {{ scoreEntry.score }}
	</div>

	<router-link to="/" class="btn btn-success">Retour à la Homepage</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default{
	name: "ResultScorePage",
  data() {
    return {
      participationScore: 0,
      totalNumberOfQuestion: 0,
      playerName: "",
      registeredScores: [],
    };
  },
	async created() {
    const info = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = info.data.size;
    this.participationScore = participationStorageService.getParticipationScore();
    this.playerName = participationStorageService.getPlayerName();
    this.registeredScores = info.data.scores;
  }
}
</script>

<style>
h1 {
	color: #198754;
}

h2 {
	color: #6bcc60;
}
</style>