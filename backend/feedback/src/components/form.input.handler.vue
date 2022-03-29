<template>
  <div class="feedback-answer" v-for="(answer, index) in id_answer[1]">
    <input class="input-answer-feedback" type="radio" v-bind:name="id_answer[0]" v-bind:value="index" required/> <label class="answer-feedback"> {{answer}}</label>
  </div>
</template>

<script>
export default {
  name: "FormInputHandler",
  props: ["id_answer"]
}
</script>

<style scoped>
.feedback-answer {
  margin: 20px 0;
}

input {
  height: 20px;
  width: 20px;
}
.input-answer-feedback {
  margin: 0 10px;
}
.answer-feedback:hover {
  color: #007cf6;
}
</style>