#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 18:20:56 2021

@author: richardlopez
"""
import random

class DoublyLinkedList: 
    
    class Node: 
        def __init__(self, data, nextNode = None, prev = None):
            self.val = data
            self.next = nextNode
            self.prev = prev
            
            
    def __init__(self): 
        self.head = None
        self.tail = None
        
    def append(self, data): 
        if self.head is None: 
            self.head = self.Node(data)
            
        else: 
            
            
            curr_node = self.head
            prev_node = None
            while curr_node != None: 
                prev_node = curr_node
                curr_node = curr_node.next 
            
            
            # after reaching the end of the
            # linked list, add the new node
            # by setting the end node to point 
            # to new node and have the new node 
            # prev pointer point to prev_node
                
            new_node = self.Node(data)
            prev_node.next = new_node
            new_node.prev = prev_node
            
                
    
    def delete(self, data): 
        pass
    
    def contains(self, data): 
        pass
    
    def __str__(self): 
        
        string_representation = "["
        
        curr = self.head
        
        
        while curr is not None: 
            if curr.next is not None:   
                string_representation += str(curr.val) + ", "
            else: 
                string_representation += str(curr.val)
            
            curr = curr.next
        
        string_representation += "]"
        
        return string_representation
        
    
    
if __name__ == "__main__": 
    myLL = DoublyLinkedList()
    
    for i in range(10): 
        num = random.randint(0, 100)
        myLL.append(num)
        
    print(myLL)
        

    
    
    
    
    
    
    
    


