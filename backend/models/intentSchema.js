const mongoose = require("mongoose")

module.exports = mongoose.model("intent", new mongoose.Schema({
    tag: {type: String, required:true, unique: true},
    pattern : {type: [String], required: true},
    flag: {type: Number, required: false},
    response: {type: Array, required: true},
    context: {type: String, required: false},
    init: {type: String, required: false},
    required: {type: String, required: false}
}))