def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    

    tree1 = []
    tree2 = []
    
    def dfs(node, tree): 
        if not node: 
            return tree.append(None)
        
        # Preorder Traversal
        
        # visit root first
        tree.append(node.val)
        
        # visit left node
        if node.left:
            dfs(node.left, tree)
        else: 
            tree.append(None)
        
        # visit right node  
        if node.right: 
            dfs(node.right, tree)
        else: 
            tree.append(None)
    
    dfs(p, tree1)
    dfs(q, tree2)
    print(tree1, tree2)
    
    if len(tree1) != len(tree2): 
        return False
    else: 
        for i in range(len(tree1)): 
            if tree1[i] != tree2[i]: 
                return False
        else: 
            return True