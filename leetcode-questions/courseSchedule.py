
def canFinish( numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    
    #build graph
    graph = { i : [] for i in range(numCourses)}
    for course, prereq in prerequisites: 
        graph[course].append(prereq)
        
        
    # perform dfs, and check to see if we are revisiting any nodes
    visited = set()
    def dfs(course): 
        if course == []: 
            return True
        elif course in visited: # if there is a duplicate
            return False
        else: 
            visited.add( course )
            
            # traverse the prereqs of the current course
            for prereq in graph[course]: 
                if not dfs( prereq ): 
                    return False
            
            graph[course] = [] # need this so dont have to search course again
            visited.remove( course ) # after done visiting, remove from graph
            return True
    
    # check every course in the graph to ensure 
    # that each course can be completed
    for course in graph.keys() : 
        if not dfs(course): 
            return False 
    
    return True


    
            
    

if __name__ == "__main__":
    print( canFinish(2, [[1,0],[0,1]]) )
        