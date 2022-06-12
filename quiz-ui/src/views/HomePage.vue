<template>
  <h1>Home page</h1>
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
    const info = await quizApiService.getQuizInfo();
    this.registeredScores = info.data.scores;
  },
};
</script>