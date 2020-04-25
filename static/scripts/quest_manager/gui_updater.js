/**d3 comes from external library. */
class QuestGui {
    /**
     * @param {Element} tree_surface - `Element` where tree will be drawn
     * @param {{}} stage_monitor - dict that descries fields binded to `Stage`  
     */
    constructor(tree_surface,
        stage_monitor) {
        this.quest = null
        this.tree_surface = tree_surface
        this.stage_monitor = stage_monitor
        this.tr_width = 800
        this.tr_height = 500

    }
    assignQuest(quest) {
        this.quest = quest
    }
    drawTree(tree, on_click) {
        // Nodes
        d3.select('svg g.nodes')
            .selectAll('circle.node')
            .data(tree.descendants())
            .enter()
            .append('circle')
            .classed('node', true)
            .attr('cx', function (d) { return d.x; })
            .attr('cy', function (d) { return d.y+10; })
            .attr('r', 15)
            .on('click', on_click);
        // Links
        d3.select('svg g.links')
            .selectAll('line.link')
            .data(tree.links())
            .enter()
            .append('line')
            .classed('link', true)
            .attr('x1', function (d) { return d.source.x; })
            .attr('y1', function (d) { return d.source.y; })
            .attr('x2', function (d) { return d.target.x; })
            .attr('y2', function (d) { return d.target.y; });

    }
    prepareSurfaceForTree() {
        console.log('here')
        this.tree_surface.innerHTML = `
        <svg width="${this.tr_width}" height="${this.tr_height + 100}">
        <g transform="translate(5, 5)">
          <g class="links"></g>
          <g class="nodes"></g>
        </g>
        </svg>
      `
    }
    updateQuestInfo(stage) {
        for (let [value_name, field] of Object.entries(this.stage_monitor)) {
            field.value = stage[value_name]
        }
    }
    update() {
        this.prepareSurfaceForTree()
        let tree = this.generateTree()
        this.drawTree(tree, (node) => this.quest.activate(node.data))
    }
    generateTree() {
        let data = this.quest.pack_as_tree()
        let root = d3.hierarchy(data)
        let treeLayout = d3.tree();
        treeLayout.size([this.tr_width, this.tr_height]);
        treeLayout(root);
        return root
    }
}
export { QuestGui }