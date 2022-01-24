const path = require("path");
const PathToStatic = path.join(__dirname, "../");

const router = require("express").Router();
const userSchema = require("../models/userSchema");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

// jwt setup
const createToken = (id) => {
  return jwt.sign({ id }, process.env.JWT_SECERT, {
    expiresIn: 24 * 60 * 60 * 1000,
  });
};

// Site Login and Register pages

router.get("/login", (req, res) => {
  res.sendFile(PathToStatic + "/public/static/loginPage.html");
});

router.post("/enterLogin", (req, res) => {
  const { username, userPassword } = req.body;
  userSchema
    .findOne({ username })
    .then((currentUser) => {
      if (currentUser) {
        bcrypt.compare(userPassword, currentUser.password, (err, result) => {
          if (result) {
            // success
            const token = createToken(currentUser._id);
            res.cookie("jwt", token, {
              httpOnly: true,
              maxAge: 24 * 60 * 60 * 1000,
            });
            res.redirect("/e/dashboard");
          } else {
            res.redirect("/user/login");
          }
        });
      } else {
        res.redirect("/user/login");
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

router.get("/register", (req, res) => {
  res.sendFile(PathToStatic + "/public/static/registerPage.html");
});

router.post("/enterRegister", (req, res) => {
  const { name, username, userPassword, userPasswordRetype } = req.body;

  // validate user data before pushing to DB
  if (
    name == "" ||
    username == "" ||
    userPassword == "" ||
    userPasswordRetype == ""
  ) {
    res.redirect("/user/login");
  }
  if (userPassword != userPasswordRetype) {
    res.redirect("/user/login");
  }
  if (userPassword.length < 8) {
    res.redirect("/user/login");
  }

  bcrypt
    .hash(userPassword, 10)
    .then((password) => {
      new userSchema({
        name: name,
        username: username,
        password: password,
      })
        .save()
        .then((newUser) => {
          console.log("new user created: ", newUser);
          res.redirect("/user/login");
        })
        .catch((err) => {
          console.log(err);
        });
    })
    .catch((err) => {
      console.log(err);
    });
});

// @desc user loging out
// @route GET /user/logout
router.get("/logout", (req, res) => {
  res.cookie('jwt', '', { maxAge: 1 });
  res.redirect("/user/login");
});

module.exports = router;
