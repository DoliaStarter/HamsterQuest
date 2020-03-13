import { Stage } from "../quest_manager/stage.js"
import { sendRequest } from "../common.js"
class Quest {
    constructor(author) {
        this.stages = {}
        this.current_stage = null
        this.description = null
        this.author = author
    }
    /**
     * Add's description to current quest.
     * @param {dict} description - dict, that contains description of current quest
     */
    addDescription(description) {
        this.description = description
    }
    /**
    * Creates data about new stage
    */
    addStage(data) {
        let new_stage_id = Object.keys(this.stages).length + 1
        let new_stage = new Stage(this.current_stage, new_stage_id, data)
        this.stages[new_stage_id] = new_stage
        this.current_stage = new_stage
    }
    /**
     * Packs current quest in dictionary
     */
    pack() {
        let packed_data = {
            "quest_id": null,
            "creator": this.author,
            "quest_data": this.description,
            "stage_data": []
        }
        const reducer = (accumulator, currentStage) => {
            accumulator.push(currentStage.pack())
            return accumulator
        }
        packed_data.stage_data = Object.values(this.stages).reduce(reducer, [])
        console.log(packed_data)
        return packed_data
    }
    /**
     * Deletes current stage
     */
    removeStage(stage_id) {
        delete this.stages[stage_id]
    }

    /**
    * Sends data to server
    */
    send() {
        let data = this.pack()
        let url = "create_quest"
        sendRequest(url, data, "POST")

    }
}
export { Quest }