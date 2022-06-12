<template>
  <h1>New Quiz page</h1>
  <form>
    <div class="input-group input-group-lg">
      <span class="input-group-text">Saisissez votre nom :</span>
      <input
        type="text"
        class="form-control"
        placeholder="Username"
        v-model="username"
        required
      />
    </div>
    <button type="button" class="btn btn-primary" @click="launchNewQuiz">
      Commencer le Quiz
    </button>
  </form>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    launchNewQuiz() {
      if (this.username == "") return;
      participationStorageService.savePlayerName(this.username);
      this.$router.push("/questions");
    },
  },
  async created() {},
};
</script>

<style>
html {
  font-family: Roboto, Arial, sans-serif;
  font-size: 28px;
  color: #666;
}

h1 {
  color: #1db623;
}

form {
  margin-top: 3em;
}

button {
  margin-top: 1em;
}

input:invalid {
  box-shadow: 0 0 10px 2px red;
}
</style>