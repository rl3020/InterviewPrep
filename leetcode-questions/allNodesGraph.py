
def shortestPathLength(graph):
    """
    :type graph: List[List[int]]
    :rtype: int
    """

    # 1. make adjacency list to represent the graph 
    g ={}
    for i, neighbors in enumerate(graph): 
        g[i] = neighbors


    min_path_length = [ float("inf") ]

    def dfs(node, visited, curr_path_length):
        if node in visited: return curr_path_length - 1
            
        visited.add( node )
        
        for neighbor in g[node]: 
            curr_path_length = dfs( neighbor, visited, curr_path_length + 1)

        if set(g.keys()) == visited: 
            if min_path_length[0] > curr_path_length: 
                min_path_length[0] = curr_path_length

        return curr_path_length + 1

    for start_node in g.keys():	
        visited = set() 
        dfs(start_node, visited, 0 )

    # single node case
    if len(g.keys()) == 1: 
        return 0

    return min_path_length[0]



print( shortestPathLength([[1], [0, 2, 3], [1], [1] ]) )


