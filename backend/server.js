const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
app.use(express.static(__dirname))
let request = require("request-promise")

// only for site
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/src/index.html');
});
app.get('/wiget', (req, res) => {
  res.sendFile(__dirname + '/src/index.html');
});
app.get('/mainPage', (req, res) => {
  res.sendFile(__dirname + '/src/mainPage.html');
});
app.get('/logPage', (req, res) => {
  res.sendFile(__dirname + '/src/logPage.html');
});

io.on('connection', (socket) => {
  console.log("user connected: ", socket.id)

  // welecoming message to new user
  io.sockets.to(socket.id).emit('resolved', JSON.stringify({
    subText : ['&#128075; Hi there this is SQU domain ChatBot', 'Ask me anythings related to SQU and I will try my best', '', 'This is beta version'],
    extend : [],
    flag : 1, 
    linker: true,
    init: null,
    notInit : true,
    additional: ['About', 'FAQ', 'Library', 'Degree Plan', 'Elearning']
  })
  )


  // user enter his request to chat module 
  socket.on("requestToResolve", (requestToResolve) => {

    const query = {
      msg : requestToResolve
    }

    var options = {
      method : 'POST',
      uri : 'http://127.0.0.1:5000/getData',
      body : query,
      json : true
    }

    request(options).then((parsedBody) => {
      console.log(parsedBody)
      let result
      result = parsedBody['result']
      // not resolved queries will be send to log sheet
      if (JSON.parse(result).flag > 19){
        let date = new Date()
        errorObject = {
          query: query.msg,
          time : `${date}`,
          id:  socket.id
        }

        io.sockets.emit('notResolved', errorObject)
      } 
      io.sockets.to(socket.id).emit('resolved', result)
    })
    .catch((err) => {
      console.log(err)
      io.sockets.to(socket.id).emit('resolved', err)
    })
  })
  // user enter request by button presented in the chat
  socket.on("requestToResolveButton", (requestToResolveButton)=> {
    request({
      method : 'POST',
      uri : 'http://127.0.0.1:5000/getInitData',
      body : requestToResolveButton,
      json : true

    }).then((parsedBody) => {
      console.log(parsedBody)
      let result
      result = parsedBody['result']
      io.sockets.to(socket.id).emit('resolved', result)
    })
    .catch((err) => {
      console.log(err)
      io.sockets.to(socket.id).emit('resolved', err)
    })
  })
});


server.listen(3000, () => {
  console.log('listening on *:3000');
});