const dialog = document.querySelector("dialog");
const addIntentButton = document.querySelector(".add-intent");
const confirmButton = document.querySelector(".confirm-button");
const discardButton = document.querySelector(".discard-button");
const addPattern = document.querySelector(".add-pattern");
const removePattern = document.querySelector(".remove-pattern");
let patternZone = document.querySelector(".pattern-zone")
let numberOfpattern = 0;
addIntentButton.onclick = () => {
  dialog.showModal();
  numberOfpattern = 0;
};
discardButton.onclick = () => {
  dialog.close();
};

addPattern.onclick = () => {
    let newPatternInput = document.createElement("input")
    newPatternInput.classList.add("stackInput")
    newPatternInput.type = "text"
    newPatternInput.name = `pattern_${numberOfpattern++}`
    patternZone.appendChild(newPatternInput)

}


