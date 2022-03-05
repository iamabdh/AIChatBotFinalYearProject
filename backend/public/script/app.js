let sendMsg = document.querySelector('#chatform')
let userInput = document.querySelector('.chatbox')
let chatList = document.querySelector('.chatlist')
let chatContainer = document.querySelector('.container-chat-box')
let submitButton = document.querySelector('.submit-button')
let socket = io()

let animationCounter = 1
let animationBubbleDelay = 20
let loading = false
let allowRecord = true

socket.on('resolved', (msg)=>{
    botResponse(msg, false)
})


sendMsg.onkeydown = (e) =>{

  if (userInput.value.length > 1) {
    submitButton.value = "send"
    allowRecord = false
  }else {
    allowRecord = true
    submitButton.value = "record"
  }

  if(!allowRecord) {
    if(e.keyCode === 13){
      e.preventDefault();

    //No mix ups with upper and lowercases
    var input = userInput.value

    //Empty textarea fix
    if(input.length > 0) {
      userResponse(input)
      userInput.value = ""
    }
  }
  }
};


submitButton.onclick = (e) => {
    alert(allowRecord)
    // if(!allowRecord){
    //   e.preventDefault();
    //   var input = userInput.value
    //
    //   //Empty textarea fix
    //   if(input.length > 0) {
    //     userResponse(input)
    //     userInput.value = ""
    //   }
    // }
}
  
const userResponse = (message) => {

    //create input
    var newChat = document.createElement('li');
    newChat.classList.add('userInput');
  
    //adds input of textarea to chatbubble list item
    newChat.innerHTML = message;
  
    //adds chatBubble to chatlist
    chatList.appendChild(newChat)  

    // emit data to server using requestToRresolve 
    socket.emit('requestToResolve', message)
}


const userResponseWithButton = (input, init, arrayButton) => {
   //create input
   var newChat = document.createElement('li');
   newChat.classList.add('userInput');
 
   //adds input of textarea to chatbubble list item
   newChat.innerHTML = input;
 
   //adds chatBubble to chatlist
   chatList.appendChild(newChat) 

   let responseToServerButton = {
     flagInit: 1,
     required: input,
     initData: init,
     additional: arrayButton 
   }
   console.log(arrayButton)
    // emit data to server using Button request
    socket.emit('requestToResolveButton', responseToServerButton)
}


const botResponse = (message, botFlag) => {
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
   
    else if (objectResponsed.flag == 2 || botFlag == true){
      if(!botFlag) {
        responseChuncked = "Which college(s) ?"
        userSelectionStuff(objectResponsed.searchFFResult)
      } else {
        responseChuncked += 'Name: ' + objectResponsed.name + '<br/>'
        responseChuncked += 'Designated: ' + objectResponsed.role + '<br/>'
        responseChuncked += 'Room: ' + objectResponsed.room + '<br/>'
        responseChuncked += 'Mobile: ' + objectResponsed.mobile + '<br/>'
        responseChuncked += 'Email: ' + objectResponsed.email  + '<br/>'
      }
    }
    else if (objectResponsed.flag == 22){
      responseChuncked += 'Please enter full name of faculty name <br>'
      responseChuncked += 'you could type <i>Dr first-name last-name</i>'
    }

    else if (objectResponsed.flag == 3) {
      bubbleStaffServices(objectResponsed.StaffServices)
      responseChuncked = "Which services ?"
    }
    else if (objectResponsed.flag == 4) {
      bubbleOnlineServices(objectResponsed.OnlineServices)
      responseChuncked = "Which services ?"
    } else if (objectResponsed.flag == 5) {
      bubbleJobServices(objectResponsed.JobServices)
      responseChuncked = "Choose position ?"
    }

    newChat.innerHTML =  responseChuncked


    chatList.appendChild(newChat)
    animateBotOutput()
    setTimeout(function(){
      chatList.scrollTop = chatList.scrollHeight;
    }, 0)

    if(objectResponsed.linker){
      userButton(
      objectResponsed.additional,
      objectResponsed.init,
      objectResponsed.notInit
      )
    }

}

const botResponseWithButton =  (response) => {
  var newChat = document.createElement('li');
  newChat.classList.add('botInput');
  newChat.innerHTML =  response;
  chatList.appendChild(newChat)
  animateBotOutput()
  setTimeout(function(){
    chatList.scrollTop = chatList.scrollHeight;
  }, 0)
}

// flag 1

const userButton = (buttonData, initData, requestNotInit) => {
 let newButtonContainer = document.createElement('div');
 newButtonContainer.classList.add('container-user-button')
  buttonData.forEach(data => {
    let newButton = document.createElement('button');
    newButton.classList.add('userButton');  
    
    newButton.onclick = () => {
      let newArrayButton = []
      buttonData.forEach(itemArray => {
        if(data != itemArray){
          newArrayButton.push(itemArray)
        }
      })
      if (!requestNotInit){ userResponseWithButton(data, initData, newArrayButton);} else {userResponse(data)}
    }
    newButton.innerHTML = data;

    newButtonContainer.appendChild(newButton)  
  })
  chatList.appendChild(newButtonContainer)
}

// flag 2
const userSelectionStuff = (buttonData) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
    for (const col in buttonData){
      let newButton = document.createElement('button');
      newButton.classList.add('userButton');
       newButton.onclick = () => {
         userResponseWithButtonCol(col)
         userSelectionCol(buttonData[col])
       }
      newButton.innerHTML = col;
      newButtonContainer.appendChild(newButton) 
    } 
  
  chatList.appendChild(newButtonContainer)
}
const userResponseWithButtonCol = (query) => {
   //create input
   var newChat = document.createElement('li');
   newChat.classList.add('userInput');
 
   //adds input of textarea to chatbubble list item
   newChat.innerHTML = query;
 
   //adds chatBubble to chatlist
   chatList.appendChild(newChat)

}

const userSelectionCol = (colObj) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  for (const order in colObj) {
    let newButton = document.createElement('button');
    newButton.classList.add('userButton');  
    newButton.innerHTML = colObj[order].name
    newButtonContainer.appendChild(newButton)
    newButton.onclick = () => {
      userResponseWithButtonCol(colObj[order].name)
      botResponse(JSON.stringify(colObj[order]), true)
    } 
  }
  chatList.appendChild(newButtonContainer)
}

// flag 3

const bubbleStaffServices = (staffServiceObj) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  for (const service in staffServiceObj){
      for (const item in staffServiceObj[service]) {
        let newButton = document.createElement('button');
        newButton.classList.add('userButton');
        newButton.onclick = () => {
          userResponseWithButtonCol(service)
          botResponseWithButton(staffServiceObj[service][item][0])
        }
        newButton.innerHTML = service;
        newButtonContainer.appendChild(newButton) 
    }
  }
  chatList.appendChild(newButtonContainer)
}

// flag 4

const bubbleOnlineServices = (onlineServices) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  for (const service in onlineServices){
      for (const item in onlineServices[service]) {
        let newButton = document.createElement('button');
        newButton.classList.add('userButton');
        newButton.onclick = () => {
          userResponseWithButtonCol(service)
          botResponseWithButton( "Redirect to: " +onlineServices[service][item])
          window.open(onlineServices[service][item],  "_blank")
        }
        newButton.innerHTML = service;
        newButtonContainer.appendChild(newButton) 
    }
  }
  chatList.appendChild(newButtonContainer)
}


// flag 5

// list position of jobs
const bubbleJobServices = (jobServices) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  for (const jobPosition in jobServices){
    let newButton = document.createElement('button');
    newButton.classList.add('userButton');

    newButton.onclick = () => {
      userResponseWithButtonCol(jobPosition)
      bubbleListPosition(jobServices[jobPosition])
    }
    newButton.innerHTML = jobPosition;
    newButtonContainer.appendChild(newButton) 
  }
  chatList.appendChild(newButtonContainer)
}

// list Department of that positions
const bubbleListPosition = (objPosition) => {
  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  for (const id in objPosition) {
    let newButton = document.createElement('button');
    newButton.classList.add('userButton');
    newButton.onclick = () => {
      userResponseWithButtonCol(objPosition[id].Department)
      listPositionOnCard(objPosition[id])
    }
    newButton.innerHTML = objPosition[id].Department;
    newButtonContainer.appendChild(newButton)     
  }
  chatList.appendChild(newButtonContainer)
}

// List Position on card 

const listPositionOnCard = (positionData) => {
  var newChat = document.createElement('li');
  newChat.classList.add('botInput');
  let responseChuncked = ""
  responseChuncked += 'College: ' + positionData.College + '<br/>'
  responseChuncked += 'Department: ' + positionData.Department + '<br/>'
  responseChuncked += 'Minimum Experience: ' + positionData.Experience + '<br/>'
  responseChuncked += 'Minimum Qualification: ' + positionData.Qualification  + '<br/>'
  responseChuncked += "Closing Date: " + positionData.Closing + '</br>'
  newChat.innerHTML =  responseChuncked;
  chatList.appendChild(newChat)
  animateBotOutput()
  setTimeout(function(){
    chatList.scrollTop = chatList.scrollHeight;
  }, 0)


  let newButtonContainer = document.createElement('div');
  newButtonContainer.classList.add('container-user-button');
  let newButton = document.createElement('button');
  newButton.classList.add('userButton');
  newButton.onclick = () => {
    userResponseWithButtonCol("Read More")
    botResponseWithButton( "Redirect to: " +positionData.link)
    window.open(positionData.link,  "_blank")
  }
  newButton.innerHTML = "Read More";
  newButtonContainer.appendChild(newButton)
  chatList.appendChild(newButtonContainer)
  
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
    console.log("Connected to Server")
 });
