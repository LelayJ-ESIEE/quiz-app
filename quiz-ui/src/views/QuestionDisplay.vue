<template>
  <div class="Question mx-auto">
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" />
    <div>
      <a
        v-for="(answer, index) in question.possibleAnswers"
        :key="answer.text"
        @click="$emit('answer-selected', index)"
        class="btn btn-light answer"
      >
        {{ answer.text }}
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object,
    },
  },
  data() {
    return {};
  },
  emits: ["answer-selected"],
};
</script>

<style>
.answer {
  margin: 0.5em 0.1em 0.5em 1em;
  width: 100%;
}

.btn:hover {
  color: #fff;
  background-color: forestgreen;
}
</style>