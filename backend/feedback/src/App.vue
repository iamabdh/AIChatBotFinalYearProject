<template>
  <Header />
  <div class="title-brand">
    AI ChatBot Feedback
  </div>
  <div class="hint-before-start">
    We are students from SQU working with ChatBot for providing information in a more easy way than traditional to SQU’students. Please fill out the questionnaire and it won’t take more than 2 minutes.
  </div>
  <div class="container-feedback">
    <FormHandler v-bind:feedbackData = "retriveFeedback"/>
  </div>
</template>

<script>
import axios from "axios"
import Header from './components/header'
import FormHandler from "@/components/form.handler";
export default {
  name: 'App',
  components: {FormHandler, Header},
  data () {
    return {
      retriveFeedback : null
    }
  },
  created() {
    // this.getFeedbackData()
    axios.get("http://127.0.0.1:3000/feedback/feedData")
      .then(res =>
          {
            this.retriveFeedback = res.data
          })
      .catch(err => console.log(err))
  },
  methods: {

  }
}
</script>

<style>
</style>
