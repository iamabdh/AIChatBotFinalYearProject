const mongoose = require("mongoose");

module.exports = mongoose.model(
    "unresolved", 
    new mongoose.Schema(
        {
            query: {type: String, required: true},
        }, 
        {
            timeseries: true
        }
    )
);
