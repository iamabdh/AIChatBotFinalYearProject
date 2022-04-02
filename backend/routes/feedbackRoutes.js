const path = require("path")
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const FeedbackSchema = require("../models/feedbackSchema")
const FeedbackFilled = require("../models/feedbackFilledSchema")
const express = require("express");
const app = express()

// redirect user to feedback page upon request
router.get("/feed", (req, res) => {
    res.redirect("index.html")
})


router.get("/feedData", (req, res) => {
    FeedbackSchema.find().then(feedbacks => {
        const sortBaseOnOrder = feedbacks.sort((a, b) => {
            return a.order - b.order
        })
        res.json(sortBaseOnOrder)
    }).catch(err => {
        console.log(err)
    })
})

router.get("/feedAnswers", (req, res) => {
    FeedbackFilled.find().then(feedbacks => {
       res.json(feedbacks)
    }).catch(err => {
        console.log(err)
    })
})


router.post("/uploadNewFeedback", (req, res) => {
    for(let feedIDItem in req.body) {
        FeedbackSchema.findById(feedIDItem).then(res => {
            if (res.mcqType){
                new FeedbackFilled({
                    questionID : feedIDItem,
                    mcqType: true,
                    answerIndex: parseInt(req.body[feedIDItem])
                }).save().then(res => {
                    console.log("new feedback entered to DB: ", res)
                }).catch(err => console.log(err))
            } else {
                new FeedbackFilled({
                    questionID : feedIDItem,
                    mcqType: false,
                    userTextTyped: req.body[feedIDItem]
                }).save().then(res => {
                    console.log("new feedback entered to DB: ", res)
                }).catch(err => console.log(err))
            }

        }).catch(err => {
            console.log(err)
            res.redirect("/")
        })
    }
    res.redirect("/")
})

module.exports = router