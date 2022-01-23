const path = require("path");
const dotenv = require("dotenv");
// Load config
dotenv.config({ path: "./config/.env" });

const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const bodyParser = require("body-parser");
app.use(express.static(__dirname));
app.use(bodyParser.urlencoded({ extended: true }));
let request = require("request-promise");
const authRoutes = require("./routes/authRoutes");
const mongoose = require("mongoose");
const expressSession = require("express-session");

// connect to database
require("./models/connectMongoDB");

// setup session

app.use(
  expressSession({
    secret: "session",
    resave: false,
    saveUninitialized: false,
  })
);

// only for site
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/static/index.html");
});
app.get("/wiget", (req, res) => {
  res.sendFile(__dirname + "/public/static/index.html");
});
app.get("/mainPage", (req, res) => {
  res.sendFile(__dirname + "/public/static/mainPage.html");
});
app.get("/logPage", (req, res) => {
  res.sendFile(__dirname + "/public/static/logPage.html");
});

// set up routes
app.use("/user", authRoutes);

io.on("connection", (socket) => {
  console.log("user connected: ", socket.id);

  // welecoming message to new user
  io.sockets.to(socket.id).emit(
    "resolved",
    JSON.stringify({
      subText: [
        "&#128075; Hello:. This is a ChatBot developped by ECE Dept Students as FYP",
        "You can ask me anything related to SQU and I will try my best",
        "",
        "Please note that this is a Beta version so you might not get full information but as log files will be maintained for unanswered queries for imporvement. Enjoy",
      ],
      extend: [],
      flag: 1,
      linker: true,
      init: null,
      notInit: true,
      additional: ["About", "FAQ", "Library", "Degree Plan", "Search Faculty"],
    })
  );

  // user enter his request to chat module
  socket.on("requestToResolve", (requestToResolve) => {
    const query = {
      msg: requestToResolve,
    };

    var options = {
      method: "POST",
      uri: "http://127.0.0.1:5000/getData",
      body: query,
      json: true,
    };

    request(options)
      .then((parsedBody) => {
        console.log(parsedBody);
        let result;
        result = parsedBody["result"];
        // not resolved queries will be send to log sheet
        if (JSON.parse(result).flag > 19) {
          let date = new Date();
          errorObject = {
            query: query.msg,
            time: `${date}`,
            id: socket.id,
          };

          io.sockets.emit("notResolved", errorObject);
        }
        io.sockets.to(socket.id).emit("resolved", result);
      })
      .catch((err) => {
        console.log(err);
        io.sockets.to(socket.id).emit("resolved", err);
      });
  });
  // user enter request by button presented in the chat
  socket.on("requestToResolveButton", (requestToResolveButton) => {
    request({
      method: "POST",
      uri: "http://127.0.0.1:5000/getInitData",
      body: requestToResolveButton,
      json: true,
    })
      .then((parsedBody) => {
        console.log(parsedBody);
        let result;
        result = parsedBody["result"];
        io.sockets.to(socket.id).emit("resolved", result);
      })
      .catch((err) => {
        console.log(err);
        io.sockets.to(socket.id).emit("resolved", err);
      });
  });
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});
