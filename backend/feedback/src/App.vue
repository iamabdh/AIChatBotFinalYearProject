<template>
  <div class="main-container">
    <Header />
    <div class="title-brand-container">
      <div class="title-brand">AI ChatBot Feedback</div>
      <div class="image-landing-container">
        <img
          src="./assets/undraw_customer_survey_re_v9cj.svg"
          alt=""
          width="500"
        />
      </div>
    </div>
    <div class="hint-before-start">
      We are students from SQU and working on a FYP (FL21-SP22) to develop a
      Chatbot for providing information to users in a more efficient way than
      traditional approach. Please fill out the questionnaire and it won’t take
      more than 2 minutes.
    </div>
    <div class="container-feedback">
      <FormHandler v-bind:feedbackData="retriveFeedback" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Header from "./components/header";
import FormHandler from "@/components/form.handler";
export default {
  name: "App",
  title: "AI Chatbot Feedback",
  components: { FormHandler, Header },
  data() {
    return {
      retriveFeedback: null,
    };
  },
  created() {
    // this.getFeedbackData()
    axios
      .get("http://127.0.0.1:3000/feedback/feedData")
      .then((res) => {
        this.retriveFeedback = res.data;
      })
      .catch((err) => console.log(err));
  },
  methods: {},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Noto+Sans&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Noto+Sans&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans&family=Quattrocento&display=swap");
* {
  margin: 0;
  padding: 0;
}
body {
  background: #ffffff;
}

.title-brand-container {
  text-align: center;
  margin-top: 30px;
  margin-bottom: 50px;
}

.title-brand {
  font-family: Abril Fatface;
  font-size: 35px;
  color: #007cf6;
  margin-bottom: 20px;
}
.hint-before-start {
  font-family: Josefin Sans;
  font-size: 20px;
  margin: 0 auto;
  width: 80%;
  line-height: 1.5;
}
.container-feedback {
  margin: 0 auto;
  width: 80%;
  font-family: Quattrocento;
  font-size: 20px;
}
</style>
