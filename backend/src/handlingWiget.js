let btn =  document.querySelector('.btn-wiget')
let wiget =  document.querySelector('.wiget-holder')
let toggol = true



btn.onclick = () => {
    if(toggol) {
        wiget.style.height = '450px'
        toggol = false
    }
    else {
        wiget.style.height = '0px'
        toggol = true
    }
  
}