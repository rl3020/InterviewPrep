
class Node: 

    def __init__(self, data, neighbors=[]): 
        self.val = data
        self.neighbors = neighbors


def teamTenure(pres):

    
    
    # step 1: 
    # perform dfs on each node to determine tenure
    all_managers = {}
    def dfs(node, curr_node_count): 
        # if no neighbors, stop doing traversal
        if node.neighbors == []: 
            return node.val, curr_node_count + 1
        else: 
            
            # keep track of num of descendants and their values
            count = [ ]
            vals = [ ]
            for neigh in node.neighbors: 
                neigh_sum , num_neighs = dfs(neigh, curr_node_count)
                count.append(num_neighs)
                vals.append(neigh_sum)

            # store the avg tenure 
            all_managers[node.val] = float((node.val + sum(vals))) / float((sum(count) + 1))
            return node.val + sum(vals), sum(count) + 1
        

    # keep track of highest tenure so far, 
    # and store the node from where it starts
    dfs(pres, 0)
    max_avg = all_managers[pres.val]
    max_node = pres.val
    for curr_node, avg in all_managers.items(): 
        if avg > max_avg: 
            max_avg = avg
            max_node = curr_node
    
    print(all_managers)
    return max_node, max_avg



if __name__ == "__main__": 
    # create graph
    pres = Node(20)
    child1 = Node(12)
    child2 = Node(18)

    pres.neighbors = [child1, child2]
    child1_neighbor1 = Node(11)
    child1_neighbor2 = Node(2)
    child1_neighbor3 = Node(3)
    child1.neighbors = [child1_neighbor1, child1_neighbor2, child1_neighbor3]

    child2_neighbor1 = Node(15)
    child2_neighbor2 = Node(8)
    child2.neighbors = [child2_neighbor1, child2_neighbor2 ]

    print( "result: ", teamTenure(pres) )



