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
            
        def __str__(self): 
            if self.val == None: 
                return "None"
            
            return str(self.val)
        
            
            
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
    
    def prepend(self, data):
        if self.head == None: 
            self.head = self.Node(data)
            return self.head
        
        
        # set the prev and next pointers for new_node
        new_node = self.Node(data)
        new_node.next = self.head
        new_node.prev = None
        
        # adjust original head pointer to have its previous be new_node
        self.head.prev = new_node
        
        # reset the head to point to new_node
        self.head = new_node
        
        return new_node
        
    
    def insert(self): 
        pass
    
        
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
        if self.head == None: 
            return 
        
        curr_node = self.head
        found = False 
        while curr_node: 
            if curr_node.val == data :
                found = True 
                break
            
            curr_node = curr_node.next
        
        if found: 
            return curr_node 
            
        
    
    def reverse(self): 
        #base case 
        if self.head  == None: 
            return 
        
        
        start = self.head 
        prev_node = None #keep track of previous node
        curr_node = start #keep track of current node
        
        while curr_node: 
            
            # use this as a temp variable to store the next node
            next_node = curr_node.next
            
            # change pointers of current node
            curr_node.next = prev_node
            curr_node.prev = next_node
            
            # move the prev_node and curr_node
            prev_node = curr_node
            curr_node = next_node
            
            
            
        self.head = prev_node
            
    def merge(self, list1, list2): 
        
        tail_node_of_l1 = None
        l1_next_node = list1.head
        
        
        while l1_next_node: 
            tail_node_of_l1 = l1_next_node
            l1_next_node = l1_next_node.next
        
        
            
            
    
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
    nums_inside = []
    
    for i in range(10): 
        num = random.randint(0, 100)
        nums_inside.append(i)
        myList.append(i)
        
    
    print(myList)
    print('Deleting 0 : ', myList.delete(nums_inside[0]) ) 
    print(myList)
    
    print("Reversing: ")
    myList.reverse()
    print(myList)
        
    print("contains 4? : ", myList.contains(4))
    
    myList.prepend(24)
    print("prepending 24: ")
    print(myList)

    
    
    
    
    
    
    
    


