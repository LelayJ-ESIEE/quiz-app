<template>
	<h1>Questionnaire</h1>
	<img v-if="question.image" :src="question.image" />
</template>

<script>
	export default{
		name: "QuestionDisplay",
		props: {
			question: {
				type: Object
  		}
		},
		emits: ["answer-selected"]
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