<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay
    :question="currentQuestion"
    @answer-selected="answerClickedHandler"
  />
</template>

<script>
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import quizApiService from "../services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "QuestionsManager",

  data() {
    return {
      currentQuestion: {},
      totalNumberOfQuestion: 0,
      currentQuestionPosition: 1,
      answers: [],
    };
  },

  components: {
    QuestionDisplay,
  },

  async created() {
    const Quizinfo = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = Quizinfo.data.size;
    await this.loadQuestionByPosition(this.currentQuestionPosition);
  },

  methods: {
    async loadQuestionByPosition(questionPosition) {
      let question = await quizApiService.getQuestion(questionPosition);
      if (question.status == 200) this.currentQuestion = question.data;
    },

    async answerClickedHandler(index) {
      this.answers.push(index);
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
        this.endQuiz();
        return;
      }
      this.loadQuestionByPosition(this.currentQuestionPosition);
    },

    async endQuiz() {
      quizApiService.postParticipation(
        participationStorageService.getPlayerName(),
        this.answers
      );
      this.$router.push("/result-score-page");
    },
  },
};
</script>

<style>
</style>