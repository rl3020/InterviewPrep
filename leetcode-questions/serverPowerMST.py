import heapq

def serverPower(connections):

    # build graph
    graph = { }
    min_weight = float("inf")
    min_node_start = None
   
    for connection in connections: 
        start, stop, weight = connection
        if weight < min_weight: 
            min_weight = weight
            min_node_start = start

        if start not in graph: 
            graph[start] = [ (weight, stop) ]
        else: 
            graph[start].append( (weight, stop) )

        if stop not in graph: 
            graph[stop] = [ (weight, start) ]
        else: 
            graph[stop].append( (weight, start) )

    print( graph, min_node_start )

    # perform primms algo
    minH = [  (min_weight, min_node_start ) ]
    heapq.heapify(minH)
    visited = set()
    mst = [ ]

    while len(visited) < len(graph.keys()): # while we havent visited all nodes
        curr_cost, curr_start = heapq.heappop(minH)
        if curr_start in visited: 
            continue
        else: 
            visited.add( curr_start )
            mst.append( [curr_cost, curr_start] )
            print( mst )

            for cost, neigh in graph[curr_start]: 
                if neigh not in visited: 
                    print("pushing onto heap: ", neigh)
                    heapq.heappush( minH, (cost, neigh) )




if __name__== "__main__": 
    
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

    print( serverPower(
        [[A,B,1],
	     [B,C,4],
	     [B,D,6],
	     [D,E,5],
	     [C,E,1]]
    ))
