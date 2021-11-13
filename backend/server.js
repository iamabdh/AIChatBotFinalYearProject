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

io.on('connection', (socket) => {
  console.log("user connected: ", socket.id)


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