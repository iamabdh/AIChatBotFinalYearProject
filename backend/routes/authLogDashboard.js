const router = require("express").Router();

const authCheck = (req, res, next) => {
  if (!req.user) {
    res.redirect("/user/login");
  } else {
    next();
  }
};

router.get("/dashboard", authCheck, (req, res) => {
  res.send("user authenticated");
});

module.exports = router;
