import { sendRequest } from "../common.js"

let quest_data = {}

class SessionMaintainer {
    constructor(data) {
        quest_data = data
        this.stages = quest_data['stages']
        this.current_stage = this.stages['stage1']
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


export { SessionMaintainer, getRadioVal, actualRadioButtonInfo}