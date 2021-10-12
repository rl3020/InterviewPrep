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
       
        curr_node = self.first
        while curr_node: 
            
            if curr_node.next != None: 
                string_rep += str(curr_node) + ", " 
            else:
                string_rep += str(curr_node)
            
            curr_node = curr_node.next 
            
        
        string_rep += "]"
        return string_rep
    
    
    def add(self, data): 
        new_node = self.QueueNode(data)
        if self.length == 0: 
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            
        self.length += 1
    
    def remove(self): 
        if self.length == 0: 
            raise Exception('Queue is empty! Cannot remove elements.')
            return
        else: 
            result = self.first.val
            self.first = self.first.next
            self.length -= 1
            return result
        
    def peek(self): 
        return self.first.val 
    
    def isEmpty(self): 
        return self.length == 0 
    
    
if __name__ == '__main__': 
    q = Queue()
    
    for i in range(0, 5): 
        print("adding: ", i)
        q.add(i)
        
    print()
    print(q)
    print() 
    print('dequeing 2xs: ', q.remove(), " ", q.remove())
    print() 
    print(q)
    
    
    
    
