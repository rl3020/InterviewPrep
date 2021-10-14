def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    #using prefix 
    
    prefix = [ 1 for i in range(len(nums)) ]
    postfix = [ 1 for i in range(len(nums)) ]
    answer = [ ]
    
    
    #create prefix array
    for i in range(0, len(nums)):
        prefix[i] = nums[i] * prefix[i - 1] if (i != 0) else prefix[i] * nums[i]
        
    #create postfix array
    for i in list(range(len(nums) - 1, -1, -1)):
        postfix[i] = postfix[i + 1] * nums[i] if i != (len(nums) - 1) else postfix[i] * nums[i]
        
    print(prefix, postfix)
        
    #get multiples of prefix and postfix array
    for j in range(len(nums)):
        
        product = 1
        if j != 0 and j != len(nums) - 1:
            product = prefix[j - 1] * postfix[j + 1]
        elif j == 0 : 
            product = 1 * postfix[j + 1]
        elif j == len(nums) - 1:
            product = prefix[j - 1] * 1
            
        answer.append(product)
        
    return answer