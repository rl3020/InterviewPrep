
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



def dfs( root ): 
    pass


if __name__ == '__main__': 
    print( "Visited graph this order: ", bfs("A", graph) )

