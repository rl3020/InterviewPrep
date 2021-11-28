def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    
    def dfs(node, new_graph_nodes={}):
        if node in new_graph_nodes: 
            return new_graph_nodes[node]
        else: 
            new_node = Node(node.val)
            new_graph_nodes[node] = new_node #store new node and map with old node
            for neighbor in node.neighbors: 
                # make sure to append 
                # all old node neighbors to new_node neighbors list
                new_node.neighbors.append( dfs(neighbor, new_graph_nodes) )
            
            return new_node
    
    if node is None: 
        return
    else: 
        return dfs(node)