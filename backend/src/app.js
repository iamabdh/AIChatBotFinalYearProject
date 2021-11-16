let sendMsg = document.querySelector('#chatform')
let userInput = document.querySelector('.chatbox')
let chatList = document.querySelector('.chatlist')
let chatContainer = document.querySelector('.container-chat-box')
let submitButton = document.querySelector('.submit-button')
let socket = io()

let animationCounter = 1
let animationBubbleDelay = 20

socket.on('resolved', (msg)=>{
    console.log(msg)
    botResponse(msg)
})





sendMsg.onkeydown = (e) =>{
    if(e.keyCode == 13){
        e.preventDefault();
  
      //No mix ups with upper and lowercases
      var input = userInput.value
  
      //Empty textarea fix
      if(input.length > 0) {
        userResponse(input)
        socket.emit('requestToResolve', input)
        userInput.value = ""
      }
    }
  };

submitButton.onclick = (e) => {
    e.preventDefault();
    var input = userInput.value
  
    //Empty textarea fix
    if(input.length > 0) {
      userResponse(input)
      socket.emit('requestToResolve', input)
      userInput.value = ""
    }
}
  
const userResponse = (message) => {
    //create input
    var newChat = document.createElement('li');
    newChat.classList.add('userInput');
  
    //adds input of textarea to chatbubble list item
    newChat.innerHTML = message;
  
    //adds chatBubble to chatlist
    chatList.appendChild(newChat)
  
  }


const botResponse = (message) => {
    var newChat = document.createElement('li');
    newChat.classList.add('botInput');
    newChat.innerHTML = message;
    chatList.appendChild(newChat)
    animateBotOutput()
    setTimeout(function(){
      chatList.scrollTop = chatList.scrollHeight;
    }, 0)
}

//change to SCSS loop
function animateBotOutput() {
  chatList.lastElementChild.style.animationDelay= (animationCounter * animationBubbleDelay)+"ms";
  animationCounter++;
  chatList.lastElementChild.style.animationPlayState = "running";
}




socket.on('connect', () => {
    console.log(socket.id); // an alphanumeric id...
 });
