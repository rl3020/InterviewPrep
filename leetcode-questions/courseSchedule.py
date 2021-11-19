def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    
    graph = {}
    
    for reqs in prerequisites: 
        course = reqs[0]
        prereq = reqs[1]
        
        if course in graph: 
            graph[course].append(prereq)
        else: 
            graph[course] = [prereq]
            
    print(graph )

if __name__ == "__main__":
    print( canFinish(2, [[1,0],[0,1]]) )
        