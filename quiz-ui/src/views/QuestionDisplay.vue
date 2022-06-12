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