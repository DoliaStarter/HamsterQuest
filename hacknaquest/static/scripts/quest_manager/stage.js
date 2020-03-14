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
    /**
     * Returns dict where exists only children id
     */
    simplified_tree() {
        let params = {
            "stage_id": this.id,
            "previous_stage_id": this.parent ? this.parent.id : null,
            "children": Object.keys(this.children).map(Number)
        }
        return Object.assign(this.data, params)
    }

    /**
     * Packs children of element in nested dict representing tree structure.
     * @param {Stage} element
     * @returns nested dict 
     */
    static to_tree(element){
        let layout = {
            stage_id:element.id,
            "previous_stage_id": element.parent ? element.parent.id : null
        }
        layout["children"] = []
        for(let child of Object.values(element.children)){
            layout["children"].push(this.to_tree(child))
        }
        Object.assign(layout, element.data)
        return layout
    }
    /**
    *  Delete all connections with this Stage
    *  @future - may be useful in future if Stage will be a tree  
    */
    delete() {
    }
}

export { Stage };