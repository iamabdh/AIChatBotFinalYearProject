const path = require("path");
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const jwt = require("jsonwebtoken");
const QueryUnresolved = require("../models/unresolvedQuerySchema");
// verify jwt token before to redirect user to dashboard
const authCheck = (req, res, next) => {
  const token = req.cookies.jwt;
  console.log(token)
  if (token) {
    jwt.verify(token, process.env.JWT_SECERT, (err, decodedToken) => {
      if (err) {
        console.log(err.message);
      } else {
        console.log(decodedToken);
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

router.get("/data", authCheck, (req, res) => {
  // QueryUnresolved.find().then(queries => {
  //   res.json(queries)
  // }).catch(err => console.log(err))
  res.send("passed")
});


module.exports = router;
