let tableView = document.querySelector('.table-view')
let tableContent = document.querySelector('.table-content')
let socket = io()


socket.on('notResolved', (errorObject)=>{
  let newRow = document.createElement('tr')
  let newContentR1 = document.createElement('th')
  let newContentR2 = document.createElement('th')
  let newContentR3 = document.createElement('th')
  newContentR1.innerHTML = errorObject.id
  newContentR2.innerHTML = errorObject.query
  newContentR3.innerHTML = errorObject.time
  newRow.appendChild(newContentR1)
  newRow.appendChild(newContentR2)
  newRow.appendChild(newContentR3)
  tableContent.appendChild(newRow)
})





socket.on('connect', () => {
    console.log(socket.id); // an alphanumeric id...
 });
