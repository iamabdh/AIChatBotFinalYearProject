const path = require("path");
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const jwt = require("jsonwebtoken");
const QueryUnresolved = require("../models/unresolvedQuerySchema");
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

})
router.get("/dashboard/data", authCheck, (req, res) => {
  QueryUnresolved.find().then(queries => {
    res.json(queries)
  }).catch(err => console.log(err))
});


module.exports = router;
