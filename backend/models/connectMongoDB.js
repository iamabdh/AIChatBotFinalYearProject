const mongoose = require("mongoose");
module.exports = mongoose.connect(
  process.env.MongoUrl,
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  },
  () => {
    console.log("MongoDB connected");
  }
);
