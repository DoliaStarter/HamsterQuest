class Stage {
    constructor(parent_id,
                own_id,
                data) {
        this.parent_id = parent_id
        this.id = own_id
        this.data = data
        // Not implemented, but in future could handle tree structure
        // this.children = []

    }
    pack() {
        let params = {
            "stage_id": this.id,
            "previous_stage_id": this.parent_id
        }
        return Object.assign(this.data, params)
    }
    /**
    *  Delete all connections with this Stage
    *  @future - may be useful in future if Stage will be a tree  
    */
    delete() {
    }
}

export { Stage };