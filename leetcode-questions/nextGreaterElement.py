
def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    
    next_greater = {}
    stack = []
    answer = []
    
    for i in range(0, len(nums2)): 
        
        if stack: 
            
            # only append values to stack in decreasing order. 
            # this ensures that values in stack don't have a next greater value. 
            
            # if the next value is greater than those already in the stack, 
            # then the current greater value is the next greater value 
            # for those already in the stack. We store the next greater value
            # for those values that are popped off the stack b/c they are
            # smaller than those in the stack. 
            
            while stack and stack[len(stack) - 1] < nums2[i]: 
                lesser_value = stack.pop()
                next_greater[ lesser_value ] = nums2[i]
                #print("adding ", lesser_value, " -> ", nums2[i])
                
            stack.append(nums2[i])
            
        else:
            stack.append( nums2[i] )
        
        
        
    for i in range(len(nums1)): 
        next_greater_value = next_greater.get(nums1[i], -1)
        answer.append(next_greater_value)
            
    return answer
            
    
    for i in range(len(nums1)): 
        next_greater_value = next_greater[ nums1[i] ]
        
        answer.append(next_greater_value)
        
    return answer
        
            
        
        
if __name__ == "__main__": 
    print( nextGreaterElement([1,3,5,6], [17,20, 3, 9, 5, 6, 7, 1]) )
        
        
        
        
