const mongoose = require("mongoose")

module.exports = mongoose.model("feedback", new mongoose.Schema({
    order   : {type: Number, required: true, unique: true},
    question: {type: String, required:true, unique: true},
    mcqType : {type: Boolean, required: true},
    answers : {type: [String], required: false},
}))