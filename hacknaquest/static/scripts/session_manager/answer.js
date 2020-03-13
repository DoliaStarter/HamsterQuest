import { sendRequest } from "../common"

class Answer{
    constructor(){
        this.text_ans = "42"
        // this.photo_ans = photo_ans
    }
    pack(){
        let answer_pack = {
            "text" : this.text_ans
        }
        return Object.assign(this.answer_pack)
    }
    send(){
        let data = this.pack()
        let url = "get_answer"
        sendRequest(url, data, "POST")
    }
}

export { Answer }