const mongoose = require("mongoose")

module.exports = mongoose.model("feedback", new mongoose.Schema({
    question: {type: String, required:true, unique: true},
    mcqType : {type: Boolean, required: true},
    answers : {type: [String], required: false},
}))