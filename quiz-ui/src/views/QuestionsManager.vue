<template>
	<h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
	<QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
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
				currentQuestion: {},
				answers: []
			};
  	},
		components: {
			QuestionDisplay
		},
		async created() {
			console.log("Composant Home page 'created'");
    	const info = await quizApiService.getQuizInfo();
    	this.totalNumberOfQuestion = info.data.size;
			await this.loadQuestionByPosition(this.currentQuestionPosition);
  	},
		methods: {
			async loadQuestionByPosition(position){
				let question = await quizApiService.getQuestion(position);
				this.currentQuestion = question.data;
			},
			async answerClickedHandler(index){
				this.answers.push(index);
				this.currentQuestionPosition++;
				this.loadQuestionByPosition(this.currentQuestionPosition);
			},
			async endQuiz(){}
		}
	}
</script>

<style>
</style>