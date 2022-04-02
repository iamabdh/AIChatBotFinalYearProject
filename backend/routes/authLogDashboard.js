const path = require("path");
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const jwt = require("jsonwebtoken");
const QueryUnresolved = require("../models/unresolvedQuerySchema");
const userSchema = require("../models/userSchema");

// verify jwt token before to redirect user to dashboard
const authCheck = (req, res, next) => {
  const token = req.cookies.jwt;
  if (token) {
    jwt.verify(token, process.env.JWT_SECERT, (err, decodedToken) => {
      if (err) {
      } else {
        next();
      }
    });
  } else {
    res.redirect("/user/login");
  }
};



router.get("/dashboard", authCheck, (req, res) => {
  res.sendFile(PathToStatic + "/public/static/dashboard.html");
});

router.get("/dashboard/user", authCheck, (req, res) => {
  const token = req.cookies.jwt;
  if (token) {
    jwt.verify(token, process.env.JWT_SECERT, (err, decodedToken) => {
      if (err) {
      } else {
        userSchema
          .findById(decodedToken.id)
          .then(userData => 
            {
              // send required data to user only basic staff not senstive data
              res.json(userData.name)
            })
          .catch(err=> console.log(err))
      }
    });
  } else {
    res.redirect("/user/login")
  }
})

router.get("/dashboard/data", authCheck, (req, res) => {
  QueryUnresolved.find().sort({_id:-1}).then(queries => {
    res.json(queries)
  }).catch(err => console.log(err))
});


module.exports = router;
