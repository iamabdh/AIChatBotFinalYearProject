<template>
  <div class="form-main-container">
    <form
        action="http://127.0.0.1:3000/feedback/uploadNewFeedback"
        method="post"
    >
      <div class="question-feedback-answer-container"
           v-for="(feedback, index) in feedbackData"
           :key="feedback.order"
      >
        <div class="question-feedback" v-if="feedback.mcqType">
          <label>
            {{index + 1}}: {{feedback.question}}
            <span class="star">*</span></label>
          <FormInputHandler v-bind:id_answer="[feedback._id, feedback.answers]"/>
        </div>
        <div class="question-feedback" v-else>
          <label> {{index + 1}}: {{feedback.question}}<span class="star">*</span></label>
          <br>
          <textarea placeholder="write your suggestions here ..." class="feedback-answer-textarea" v-bind:name="feedback._id" required/>
        </div>
      </div>
      <input type="submit" value="submit" class="feedback-submit"/>
    </form>
  </div>
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
.form-main-container {
  margin: 40px 0;
}

.question-feedback-answer-container {
  margin: 50px 0;
}
  .star{
    margin: 0 5px;
    color: #ff0000;
  }
  .feedback-answer-textarea {
    margin: 20px 10px;
    width: 60%;
    height: 200px;
    padding: 10px;
    border:3px dashed indigo;
    background-color:aliceblue;
    resize: none;
  }
input[type="submit"] {
  display: block;
  margin: 0 auto;
  width: 30%;
  margin-top: 30px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  color: #ffffff;
  font-size: 20px;
  background-color: #25a5be;
}

input[type="submit"]:hover {
  background-color: coral;
}

</style>