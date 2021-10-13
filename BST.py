#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:59:45 2021

@author: richardlopez
"""
import random

class Tree: 
    
    class TreeNode: 
        
        def __init__(self, data): 
            self.val = data
            self.left = None
            self.right = None 
            
        def __str__(self): 
            return str(self.val) if self.val != None else 'None'
        
        
    def __init__(self): 
        self.root = None
        
    def __str__(self): 
        str_rep = "Tree: ["

        stack = []
        visited = []
        if self.root: 
            stack.append(self.root)
            root = self.root
            
            while stack: 
            
                if root.left and root.left not in visited: 
                    stack.append(root.left)
                    root = root.left
                    continue 

                curr_node = stack.pop()
                str_rep += " " + str(curr_node)
                visited.append(root)

                if root.right and root.right not in visited: 
                    stack.append(root.right)
                    root = root.right


            str_rep += "]"
            return str_rep

        else: 
            return "Empty Tree :/"

        
        
        
    def insert(self, data): 
        if self.root: 
            self._insert(data, self.root)
        else: 
            self.root = self.TreeNode(data)
            
            
    def _insert(self, data, root): 
        
        if root: 
            if data < root.val: 
                if root.left: 
                    self._insert(data, root.left)
                else: 
                    root.left = self.TreeNode(data)
            
            elif data > root.val: 
                if root.right: 
                    self._insert(data, root.right)
                else: 
                    root.right = self.TreeNode(data)
            else: 
                print("duplicate value being inserted!")

        else: 
            root = self.TreeNode(data)
            
    def inOrderTraversal(self): 
        if self.root: 
            self._inorder(self.root)
        else: 
            print("root is empty")

    def _inorder(self, root): 
        if root: 
            if root.left: 
                self._inorder( root.left )

            print(root)

            if root.right: 
                self._inorder( root.right )
    
    
if __name__ =='__main__': 
    tree = Tree()
    nums_inserted = [ ]
    for i in range(0, 10): 
        num = random.randint(0, 100)
        nums_inserted.append(num)
        tree.insert(num)

    print("numbers inseretd: ", nums_inserted)
    print("my __str__: ", tree)
    print("actual tree: ")
    tree.inOrderTraversal()







