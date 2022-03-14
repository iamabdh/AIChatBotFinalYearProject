let socket = io()
let tableView = document.querySelector('.table-view')
let tableContent = document.querySelector('.table-content')
const dialog = document.querySelector("dialog");
const addIntentButton = document.querySelector(".add-intent");
const confirmButton = document.querySelector(".confirm-button");
const discardButton = document.querySelector(".discard-button");
const addPattern = document.querySelector(".add-pattern");
const removePattern = document.querySelector(".remove-pattern");
let patternZone = document.querySelector(".pattern-zone")
const userName = document.querySelector(".user-profile .user-name");


// addIntentButton.onclick = () => {
//   dialog.showModal();
//   numberOfpattern = 0;
// };
// discardButton.onclick = () => {
//   dialog.close();
// };

// addPattern.onclick = () => {
//     let newPatternInput = document.createElement("input")
//     newPatternInput.classList.add("stackInput")
//     newPatternInput.type = "text"
//     newPatternInput.name = `pattern_${numberOfpattern++}`
//     patternZone.appendChild(newPatternInput)
// }


const UnresolvedQueries = async () => {
    const res = await fetch("/e/dashboard/data");
    const retriveData = await res.json();
    retriveData.forEach(item => {
        // create new table'tag
        let newRow = document.createElement('tr')
        let newContentR1 = document.createElement('th')
        let newContentR2 = document.createElement('th')
        newContentR1.innerHTML = item.query
        newContentR2.innerHTML = item.createdAt
        newRow.appendChild(newContentR1)
        newRow.appendChild(newContentR2)
        tableContent.appendChild(newRow)
    })
}

UnresolvedQueries()
socket.on('notResolved', ()=> {UnresolvedQueries()})

// load user infos to page 

const LoadUserData = async () => {
    const res = await fetch("/e/dashboard/user");
    const retriveData = await res.json()
    userName.innerHTML = retriveData

}


LoadUserData()

