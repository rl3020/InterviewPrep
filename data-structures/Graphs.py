
# graph implementation using adjacency list

graph = {
    "A": ["B", "D"], 
    "B": ["C", "F"], 
    "C": ["G", "E"],
    "D": ["F"],
    "E": ["B", "F"],
    "F": ["A"],
    "G": ["E"]
}

def bfs( root, graph ): # Pass in A, for example
    queue = []
    queue.append(root)
    visited = set()
    ordered_visit = []
    while queue: 
        curr_node = queue.pop(0)
        visited.add(curr_node)

        # this is just to keep track of the 
        # order of the visit of each node. 
        # still need to make sure node wasn't visited
        if curr_node not in ordered_visit: 
            ordered_visit.append(curr_node)
        
        for neighbor in graph[curr_node]: 

            if neighbor not in visited: 

                queue.append(neighbor)
            
    return " ".join( ordered_visit )

def dfs( root, graph, visited=set()): 
    if root == None: 
        return 
    else: 
        result = _dfs(root, graph)
        return result

def _dfs(root, graph, visited=set(), ordered=[]): 

    visited.add(root)
    if root not in ordered: 
        ordered.append(root)

    for neighbor in graph[root]: 

        # only visit the neighbor if 
        # it has not been visited 
        if neighbor not in visited: 
            _dfs(neighbor, graph, visited, ordered)

    if len(list(visited)) == len(graph.keys()): 
        return " ".join(ordered)
        

if __name__ == '__main__': 
    print( "BFS: ", bfs("A", graph) )
    print( "DFS: ", dfs("A", graph) )
