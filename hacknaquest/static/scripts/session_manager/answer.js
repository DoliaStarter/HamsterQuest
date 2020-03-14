import { sendRequest } from "../common.js"

let quest_data = {
    "quest_title": "cool quest",
    "quest_description": "Lorem ipsum dolor sit amet,consectetur adipiscing elit. Pellentesque lectus mi, mollis id tincidunt ac, mattis sed magna. Nullam euismod quam eu auctor sodales. Fusce libero tortor, vulputate sit amet euismod sed, commodo nec justo. Nam sodales tortor in ex fermentum, in semper nisl lobortis. Ut elementum tristique velit at fermentum. Quisque eu eros egestas, placerat enim non, laoreet ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer sit amet hendrerit turpis. ",
    "author": "A writer",
    "stages": {
        "stage1": {
            "task": "some task",
            "location": "12.0444404;12.4564888",
            "status": "actual queststate", // not stareted, started, completed
            "is_completed": false,
            "answers": {
                // correct answer: next stage
                "42": "stage2",
                "answer": "stage3",
            }
        },
        "stage2": {
            "task": "task",
            "location": "location",
            "status": "status",
            "is_completed": false,
            "answers": {
                // If null ->  finish quest
                "10": "stage1",
                "23": null
            }
        },
        "stage3": {
            "task": "task",
            "location": "location",
            "status": "status",
            "is_completed": false,
            "answers": {
                "10": "stage1",
                "11": null
            }
        }
    }
}


class SessionMaintainer {
    constructor(/*gui*/) {
        //this.gui = gui 
        //this.text_ans = gui.text_ans
        this.stages = quest_data["stages"]
        this.current_stage = this.stages["stage1"]
        this.finished = {
            "text": " Congatulations !"
        }

        // this.photo_ans = photo_ans
    }
    
    getQuestData() {
        sendRequest("get_data", '', "GET").then(
            (data) => {
                // handle data
                console.log(data)
                this.data = data
            }
        )
    }

    updateData() {
        for (let [text_field, updater] in Object.entries(this.gui)) {
            updater(this.current_stage[text_field])
        }
    }
    
    pack() {
        let user = sessionStorage.getItem('username')
        let answer_pack = {
            "username": user,
            "text": this.text_ans
        }

        return answer_pack
    }
    /**
     * @param {string} answer - users answer on quest
     */
    check_answer(answer) {
        let answers = Object.keys(this.current_stage.answers)
        if (answers.includes(answer["answer"])) {
            let next_stage = this.current_stage.answers["answer"]
            console.log("next_stage")
            console.log(this.current_stage.answers)
            this.current_stage = this.stages[next_stage] || this.finished
            console.log("this.current_stage")
            console.log(this.current_stage)
            //updateData()
        }
    }
    send() {
        let data = this.pack()
        let url = "get_answer"
        sendRequest(url, data, "POST")
    }

    //TODO getData(){}
    //TODO checkAnswer(){}
    //TODO activateStage(){}
}

function sendDict(){
    let data = quest_data['stages']
    let url = "get_data"
    sendRequest(url, data, "POST")
}

/**
 * 
 * @param {Document.getElementBy*} form - get form where radiobuttons is
 * @param {string} name - will check radio buttons only with same names
 */
function getRadioVal(form, name) {
    var val;
    var radios = form.elements[name];
    
    for (var i=0, len=radios.length; i<len; i++) {
        if ( radios[i].checked ) { 
            val = radios[i].value; 
            break; 
        }
    }
    return val; 
}

/**
 * 
 * @param {string} radioVal - name of radio button what must be checked 
 * @returns {dict} - information of stage radioVal
 */
function actualRadioButtonInfo(radioVal){
    var stages = quest_data['stages']
    return stages[radioVal]
}


export { SessionMaintainer, quest_data, getRadioVal, actualRadioButtonInfo, sendDict}