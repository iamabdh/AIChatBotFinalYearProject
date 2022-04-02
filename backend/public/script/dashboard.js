let socket = io()
let tableView = document.querySelector('.table-view')
let tableContent = document.querySelector('.table-content')
const userName = document.querySelector(".user-profile .user-name");
let tableContentFeed = document.querySelector(".feedback-content")

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
// function will be triggered when client window gets refreshed
LoadUserData()




// feedback

const getDataFeedback = async () => {
    // get feed Questions
    const getFeedData = await fetch("/feedback/feedData")
        .then((res) => {return res.json()})
        .catch((err) => {return err})

    const getFeedAnswers = await fetch("/feedback/feedAnswers")
        .then((res) => {return res.json()})
        .catch((err) => {return err})
    const totalResponses = Object.keys(getFeedAnswers).length / Object.keys(getFeedData).length
    // populate data as required
    getFeedData.forEach((questionItem) => {
        if(questionItem.mcqType) {
            let totalOfAnswers =  questionItem.answers.length;
            let answerPercentage = new Array(totalOfAnswers).fill(0);
            getFeedAnswers.forEach((answerItem) => {
                if(questionItem._id === answerItem.questionID) {
                    answerPercentage[answerItem.answerIndex] +=1;
                }
            })
            answerPercentage.forEach((answerPercentageItem, indexItem) => {
                answerPercentage[indexItem] = ((answerPercentageItem/totalResponses) * 100).toPrecision(2);
            })
            createTableFeedback(true, questionItem.question, questionItem.answers, answerPercentage)
        } else {

        }

    })
}

getDataFeedback()

const createTableFeedback = (mcqType, question, answers, answersPercentage) => {
    if (mcqType) {
        let newTable = document.createElement("table")
        let newRowQuestion = document.createElement('tr')
        let rowQuestionContent = document.createElement("th")
        let newRowHeading = document.createElement("tr")
        let rowQuestionAnswerHeading =  document.createElement("th")
        let rowQuestionPercentageHeading = document.createElement("th")
        rowQuestionContent.innerHTML = question
        rowQuestionAnswerHeading.innerHTML = "Answers"
        rowQuestionPercentageHeading.innerHTML = "Percentage"
        newRowQuestion.appendChild(rowQuestionContent)
        newRowHeading.appendChild(rowQuestionAnswerHeading)
        newRowHeading.appendChild(rowQuestionPercentageHeading)
        newTable.appendChild(newRowQuestion)
        newTable.appendChild(newRowHeading)
        answers.forEach((answerItem, indexItem) => {
          let newRow = document.createElement('tr');
          let rowAnswer = document.createElement("th");
          let rowPercentage = document.createElement("th");
          rowAnswer.innerHTML = `${indexItem + 1} ) ${answerItem}`;
          rowPercentage.innerHTML= `${answersPercentage[indexItem]}%`;
          newRow.appendChild(rowAnswer);
          newRow.appendChild(rowPercentage);
          newTable.appendChild(newRow)
        })
        tableContentFeed.appendChild(newTable)
    } else {

    }
}