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
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods:{
    launchNewQuiz(){
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  },
  async created() {
  }
};
</script>

<style>
h1 {
  color: #198754;
}
</style>
