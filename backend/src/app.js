let data = document.querySelector('.data')
let send = document.querySelector('.send')
let socket = io()

send.onclick = () => {
    if(data.value){
        socket.emit('requestToResolve', data.value)
        data.value = ''
    }
}


socket.on('resolved', (msg)=>{
    console.log(msg)
    document.querySelector('.data-res').innerHTML = msg
})


socket.on('connect', () => {
    console.log(socket.id); // an alphanumeric id...
 });

