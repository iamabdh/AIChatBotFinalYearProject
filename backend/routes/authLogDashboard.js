const path = require("path");
const PathToStatic = path.join(__dirname, "../");
const router = require("express").Router();
const jwt = require("jsonwebtoken");

// verify jwt token before to redirect user to dashboard
const authCheck = (req, res, next) => {
  const token = req.cookies.jwt;

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

module.exports = router;
