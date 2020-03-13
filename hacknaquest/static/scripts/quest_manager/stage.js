class Stage {
    constructor(parent,
                own_id,
                data) {
        this.parent = parent
        this.id = own_id
        this.data = data
        this.children = {}
        if(parent) parent.register_child(this)

    }

    register_child(child){
        this.children[child.id] = child
    }
    pack() {
        let params = {
            "stage_id": this.id,
            "previous_stage_id": this.parent ? this.parent.id : null,
            "children": Object.keys(this.children).map(Number)
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