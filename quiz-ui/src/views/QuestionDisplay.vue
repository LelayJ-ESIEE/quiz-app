<template>
	<h2>{{ question.title }}</h2>
	<img v-if="question.image" :src="question.image" />
	<p>{{ question.text }}</p>
	<div>
		<a v-if="question.possibleAnswers" @click="$emit('answer-selected', 1)">
			A : {{ question.possibleAnswers[0].text }}</a> <br>
		<a v-if="question.possibleAnswers" @click="$emit('answer-selected', 2)">
			B : {{ question.possibleAnswers[1].text }}</a> <br>
		<a v-if="question.possibleAnswers" @click="$emit('answer-selected', 3)">
			C : {{ question.possibleAnswers[2].text }}</a> <br>
		<a v-if="question.possibleAnswers" @click="$emit('answer-selected', 4)">
			D : {{ question.possibleAnswers[3].text }}</a>
	</div>
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