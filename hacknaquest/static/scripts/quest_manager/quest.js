import { Stage } from "../quest_manager/stage.js"
import { sendRequest } from "../common.js"
class Quest {
    constructor(author, gui) {
        this.stages = {}
        this.current_stage = null
        this.description = null
        this.author = author
        this.root = null
        this.gui = gui
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
        // Changed from int to string
        let new_stage_id = data.stage_title 
        // refers to keys
        if(new_stage_id in this.stages) 
        {
            alert("Quest already created! ")
            return
        }
        // Object.keys(this.stages).length + 1
        let new_stage = new Stage(this.current_stage, new_stage_id, data)
        if (!this.root) this.root = new_stage
        this.stages[new_stage_id] = new_stage
        this.current_stage = new_stage
        this.gui.update()
    }
    activate(node) {
        this.current_stage = this.stages[node.stage_id]
        /**fix */
        this.gui.updateQuestInfo(node)
    }

    pack_as_tree() {
        let tree = Stage.to_tree(this.root)
        return tree
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
        let stage_tree = this.pack_as_tree()
        let quest_params = {
            "quest_id": null,
            "creator": this.author,
            "quest_data": this.description,
            "stage_tree": stage_tree
        }
        console.log(quest_params)
        let url = "create_quest"
        sendRequest(url, quest_params, "POST")

    }
}
export { Quest }