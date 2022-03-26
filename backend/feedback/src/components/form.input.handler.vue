<template>
  <div class="feedback-answer" v-for="(answer, index) in id_answer[1]">
    <input type="radio" v-bind:name="id_answer[0]" v-bind:value="index" required/> <label> {{answer}}</label>
  </div>
</template>

<script>
export default {
  name: "FormInputHandler",
  props: ["id_answer"]
}
</script>

<style scoped>

</style>