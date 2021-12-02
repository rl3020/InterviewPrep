from collections import deque 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        tree = [ ]
        q = deque()
        q.append(root)
        
        while q: 
            curr_node = q.popleft()
            
            tree.append( curr_node.val if curr_node else None )
            
            if not curr_node:
                continue
            
            if curr_node.left:
                q.append(curr_node.left)
            else: 
                q.append(None)
                
            if curr_node.right:
                q.append(curr_node.right)
            else:
                q.append( None )
            
            
        tree = [ str(char) for char in tree ]
        tree = ",".join(tree)
        return tree
        
    
    # [ 1, 2, 3, none, none, 4, 5, none, none, none, none]
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(",")
        new_data = []
        for elem in data: 
            if elem == "None": 
                new_data.append( None )
            else: 
                new_data.append( int(elem) ) 
                
        root = TreeNode(new_data[0]) if new_data[0] != None else None
        q = deque()
        q.append(root)
        i = 1
        
        while i < len(new_data) - 1:
            
            curr_node = q.popleft()
            
            if not curr_node: 
                continue
            
            
            if new_data[i] != None: 
                left_node = TreeNode( new_data[i] ) 
            else: 
                left_node = None
                
                
            if new_data[i + 1] != None: 
                right_node = TreeNode( new_data[ i + 1 ])
            else: 
                right_node = None   
            

            curr_node.left = left_node
            curr_node.right = right_node
            
            q.append(left_node)
            q.append(right_node)
            
            i += 2
            
            
        return root
        


