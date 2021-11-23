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
    responseChuncked = ''
    responseTable = ''
    objectResponsed = JSON.parse(message)
    if (objectResponsed.flag == 0) {
      responseChuncked = objectResponsed.response
    } 

    else if (objectResponsed.flag ==20) {
      responseChuncked = objectResponsed.response
    }
    else if(objectResponsed.flag == 1){
     
      objectResponsed.subText.forEach(item => {
        responseChuncked +=  item+ ' <br/>'
      });
      if ( objectResponsed.extend !=null){
        objectResponsed.extend.forEach(item => {
          responseChuncked +=  item+ ' <br/>'
        });
      }
      
    }
   
    else if (objectResponsed.flag == 2){
      responseChuncked += 'Name: ' + objectResponsed.name + '<br/>'
      responseChuncked += 'Designated: ' + objectResponsed.role + '<br/>'
      responseChuncked += 'Room: ' + objectResponsed.room + '<br/>'
      responseChuncked += 'Mobile: ' + objectResponsed.mobile + '<br/>'
      responseChuncked += 'Email: ' + objectResponsed.email  + '<br/>'
    }

    else if (objectResponsed.flag == 22){
      responseChuncked += 'Please enter full name of faculty name <br>'
      responseChuncked += 'you could type <i>Dr name name</i>'
    }

    newChat.innerHTML =  responseChuncked

    chatList.appendChild(newChat)
    animateBotOutput()
    setTimeout(function(){
      chatList.scrollTop = chatList.scrollHeight;
    }, 0)
}

function animateBotOutput() {
  chatList.lastElementChild.style.animationDelay= (animationCounter * animationBubbleDelay)+"ms";
  animationCounter++;
  chatList.lastElementChild.style.animationPlayState = "running";
}


// const changeBorderError = () => {
//   document.querySelector('.botInput').style.borderTop = '#ff0000'
// }

socket.on('connect', () => {
    console.log(socket.id); // an alphanumeric id...
 });
