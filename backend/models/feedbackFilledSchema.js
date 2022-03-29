const mongoose = require("mongoose")

module.exports = mongoose.model("feedbackFilled", new mongoose.Schema({
    questionID: {type: String, required:true},
    mcqType: {type: Boolean, required: true},
    answerIndex : {type: Number, required: false},
    userTextTyped : {type: String, required: false}
}))