<template>
	<h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
	<QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
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
		}
	}
</script>

<style>
</style>