const mongoose = require("mongoose");

module.exports = mongoose.model(
  "user",
  new mongoose.Schema({
    name: { type: String, require: true },
    username: { type: String, require: true, unique: true },
    password: { type: String, require: true },
    editor: { type: Boolean, default: false, require: false },
  })
);
