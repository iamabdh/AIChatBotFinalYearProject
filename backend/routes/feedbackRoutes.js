const path = require("path")
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const FeedbackSchema = require("../models/feedbackSchema")
const FeedbackFilled = require("../models/feedbackFilledSchema")




router.get("/feedData", (req, res) => {
    FeedbackSchema.find().then(feedbacks => {
        res.json(feedbacks)
    }).catch(err => {
        console.log(err)
    })
})

module.exports = router