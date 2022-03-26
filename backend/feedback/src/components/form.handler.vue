<template>
  <form
      action="http://127.0.0.1:3000/feedback/uploadNewFeedback"
      method="post"
  >
    <div v-for="feedback in feedbackData">
      <label class="question-feedback" v-if="feedback.mcqType">
        {{feedback.question}}
        <FormInputHandler v-bind:id_answer="[feedback._id, feedback.answers]"/>
      </label>
    </div>
    <div v-for="feedback in feedbackData">
      <div v-if="!feedback.mcqType">
        <label class="question-feedback" >
          {{feedback.question}}
        </label>
        <textarea v-bind:name="feedback._id" required/>
      </div>
    </div>
    <input type="submit" value="submit"/>
  </form>
</template>

<script>
import FormInputHandler from "@/components/form.input.handler";

export default {
  name: "FormHandler",
  components: {FormInputHandler},
  props: ["feedbackData"]
}
</script>

<style scoped>

</style>