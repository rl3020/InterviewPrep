#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 18:20:56 2021

@author: richardlopez
"""
import random

#linked list
class DoublyLinkedList: 
    
    class Node: 
        def __init__(self, data, nextNode = None, prev = None):
            self.val = data
            self.next = nextNode
            self.prev = prev
            
            
    def __init__(self): 
        self.head = None
        self.tail = None
        
    
    # append node to list
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
        
        
        
        prev = None 
        start = self.head
        curr_node = start
        
        found = False
        while curr_node: 
            if curr_node.val == data: 
                found = True 
                break 
            
            prev = curr_node
            curr_node = curr_node.next
        
        if found:
            if prev: 
                prev.next = curr_node.next
            elif prev == None: 
                self.head = curr_node.next
            
            
            if curr_node.next: 
                curr_node.next.prev = prev
        
            return curr_node.val
            
    
    def contains(self, data): 
        pass
    
    def reverse(self): 
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
    myList = DoublyLinkedList()
    nums_inside = [ ]
    
    for i in range(1): 
        num = random.randint(0, 100)
        nums_inside.append(num)
        myList.append(num)
        
    
    print(myList)
    print('Deleting: ', nums_inside[0])
    print(myList.delete(nums_inside[0]))
    print(myList)
        

    
    
    
    
    
    
    
    


