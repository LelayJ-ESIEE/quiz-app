<template>
  <h1>New Quiz page</h1>
  <form>
    <div>
      <p>Saisissez votre nom :</p>
      <input type="text" placeholder="Username" />
    </div>
    <button class="btn btn-success">Commencer le quiz</button>
  </form>
</template>

<script>
// import quizApiService from "@/services/QuizApiService";

export default {
  name: "NewQuizPage",
  data() {
    return {
    };
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
