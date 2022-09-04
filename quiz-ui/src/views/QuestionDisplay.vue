<template>
	<h1>Questionnaire</h1>
	<h2>{{ question.title }}</h2>
	<img v-if="question.image" :src="question.image" />
	<p>{{ question.text }}</p>
	<a v-for="(answer, index) in question.possibleAnswers" v-bind:key="answer.text"
		@click="$emit('answer-selected', index)">
		{{ answer.text }}
	</a>
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