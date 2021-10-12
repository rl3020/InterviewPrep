#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:49:10 2021

@author: richardlopez
"""

class Stack: 
    
    class StackNode: 
        
        def __init__(self, data): 
            self.val = data
            self.next = None
        
        def __str__(self): 
            return str(self.val)


    def __init__(self): 
        self.top = None
        self.length = 0 
        
    def __str__(self): 
        if self.top == None: 
            return '[]'
        
        string_representation = " top -> ["
        curr_node = self.top
        
        while curr_node: 
            string_representation += str(curr_node.val)
            if curr_node.next: 
                string_representation += " ,"
                
            curr_node = curr_node.next
        
        string_representation += "]"
        
        return string_representation
        
        
    def push(self, data):
        new_node = self.StackNode(data)
        old_node = self.top
        new_node.next = old_node
        self.top = new_node
        self.length += 1
        
        return new_node
        
        
    def pop(self): 
        
        if self.length == 0: 
            raise Exception('Empty list. Cannot pop.')
        else: 
            to_return = self.top.val
            self.top = self.top.next
            self.length -= 1
            return to_return 
            
        
    def peek(self): 
        if self.top == None: raise Exception('Empty list. Cannot pop.')
        else: return self.top.val
        
    def isEmpty(self): 
        return self.length == 0
    
    
    
if __name__ == '__main__': 
    
    stack = Stack()
    for i in range(0, 10): 
        stack.push(i)
    
    print( "current stack: ",stack )
    
    for i in range(0, 5): 
        print( "popping top: ", stack.pop() )
        
    
    print( "stack after all pops: ", stack )
    print( "peeking at next value: ", stack.peek() )  
    
    print( "Emptying stack..." )
    
    for i in range( 0, stack.length ): 
        stack.pop()
        
    print( "stack.isEmpty(): ", stack.isEmpty() )





