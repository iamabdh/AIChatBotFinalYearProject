const path = require("path");
const PathToStatic = path.join(__dirname, "../");

const router = require("express").Router();
const userSchema = require("../models/userSchema");
const bcrypt = require("bcryptjs");

// Site Login and Register for admin

router.get("/login", (req, res) => {
  res.sendFile(PathToStatic + "/public/static/loginPage.html");
});

router.post("/enterLogin", (req, res) => {});

router.get("/register", (req, res) => {
  res.sendFile(PathToStatic + "/public/static/registerPage.html");
});

router.post("/enterRegister", (req, res) => {
  new userSchema({
    name: req.body.name,
    username: req.body.username,
    password: req.body.userPassword,
  })
    .save()
    .then((newUser) => {
      console.log("new user created: ", newUser);
      res.redirect("/user/login");
    })
    .catch((err) => {
      console.log(err);
    });
});

module.exports = router;
