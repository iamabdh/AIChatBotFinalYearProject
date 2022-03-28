
submitButton.onclick = () => {
    if(allowRecord){
        let speech = true
        userInput.disabled  = true
        submitButton.value = "recording"
        RecordingState()
        window.SpeechRecognition = window.webkitSpeechRecognition

        const recognition = new SpeechRecognition();

        recognition.interimResults = true;

        recognition.addEventListener('result', e=> {
            const transcript = Array.from(e.results)
                .map(result => result[0])
                .map(result => result.transcript)
            const isFinished = Array.from(e.results).map(result => result.isFinal)
            if (allowRecord) {
                userInput.value = transcript
            }
            if(isFinished[0]){
                userResponse(transcript[0])
                userInput.value = ""
                userInput.disabled  = false
                UnrecodingState()
                submitButton.value = "record"
            }
        })

        if (speech == true) {
            recognition.start();
        }
    }
}



const RecordingState = () => {
submitButton.style.backgroundColor = "#17e93a"
submitButton.style.border = "2px solid #17e93a"
submitButton.style.color = "#000"
}
const UnrecodingState = () => {
submitButton.style.backgroundColor = "#e9a617"
submitButton.style.border = "2px solid #e9a617"
submitButton.style.color = "#fff"
}