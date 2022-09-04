<template>
  <h1>New Quiz page</h1>
  <form>
    <div>
      <p>Saisissez votre nom :</p>
      <input type="text" placeholder="Username" v-model="username" />
    </div>
    <button class="btn btn-success" @click="launchNewQuiz">Commencer le quiz</button>
  </form>
</template>

<script>
import participationStorageService from "@/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods:{
    launchNewQuiz(){
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  },
  async created() {
		console.log("Composant New Quiz page 'created'");
  }
};
</script>

<style>
h1 {
  color: #198754;
}
</style>
