<template>
  <Header />
  <div class="title-brand">
    AI ChatBot Feedback
  </div>
  <div class="hint-before-start">
    We are students from SQU working with ChatBot for providing information in a more easy way than traditional to SQU’students. Please fill out the questionnaire and it won’t take more than 2 minutes.
  </div>
  <div class="container-feedback">
    <FormHandler />
  </div>
</template>

<script>

import Header from './components/header'
import FormHandler from "@/components/form.handler";
export default {
  name: 'App',
  components: {FormHandler, Header},
}
</script>

<style>
</style>
