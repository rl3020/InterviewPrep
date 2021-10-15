def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    max_sum = -10000 
    current_sum = 0 
    
    for num in nums: 
        
        current_sum += num
        
        if current_sum < num: 
            current_sum = num
            
        max_sum = max(max_sum, current_sum)
        
    return max_sum


if __name__ == '__main__': 
    print( maxSubArray([5,4,-1,7,8]) )