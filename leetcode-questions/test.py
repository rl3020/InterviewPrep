
class Tree: 

    class Node: 

        def __init__(self, val, left, right): 
            self.val = val 
            self.left = left
            self.right = right


    def __init__(self, tree_arr): 
        def createTree(tree, root):

            curr_row = ["left", "right"]
            curr_node = root 

            for i , elem in enumerate(tree): 
                
                curr_node_type = curr_row[ i % len(curr_row)]
                if curr_node_type == "left": 
                    curr_node.left = self.Node(elem)

        createTree(tree_arr)




def rec(arr): 

    for i in range(0 , 10): 
        arr.append(i)

    return arr
        



if __name__== '__main__': 

    li = []
    rec(li)
    print( "After recursion: ",li )

    