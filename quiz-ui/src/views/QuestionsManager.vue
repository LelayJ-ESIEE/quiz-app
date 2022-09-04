<template>
	<h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
	<QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
	import QuestionDisplay from './QuestionDisplay.vue';
	import quizApiService from "@/services/QuizApiService";

	export default{
		name: "QuestionsManager",
		data() {
			return {
				totalNumberOfQuestion: 0,
				currentQuestionPosition: 1,
			};
  	},
		components: {
			QuestionDisplay
		},
		async created() {
			console.log("Composant Home page 'created'");
    	const info = await quizApiService.getQuizInfo();
    	this.totalNumberOfQuestion = info.data.size;
  	}
	}
</script>

<style>
</style>