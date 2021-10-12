#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:38:49 2021

@author: richardlopez
"""

class Queue: 
    
    class QueueNode: 
        
        def __init__(self, data): 
            self.val = data
            self.next = None
        
        def __str__(self): 
            return str(self.val) if self.val != None else 'None'
        
    
    def __init__(self): 
        self.length = 0 
        self.first = None
        self.last = None
        
    def __str__(self): 
        string_rep = "["
        values = ""
        
        curr_node = self.last
        while curr_node: 
            
            if curr_node.next != None: 
                values = ", " + str(curr_node) + values
            else:
                values = str(curr_node) + values
            
            curr_node = curr_node.next 
            
        string_rep += values
        string_rep += "]"
        return string_rep
    
    
    def add(self, data): 
        new_node = self.QueueNode(data)
        if self.length == 0: 
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last 
            self.last = new_node
            
        self.length += 1
    
    def remove(self): 
        pass
    
    def peek(self): 
        pass
    
    def isEmpty(self): 
        pass
    
    
if __name__ == '__main__': 
    q = Queue()
    
    for i in range(0, 10): 
        print("adding: ", i)
        q.add(i)
    
    print(q)
    
    
    
    
