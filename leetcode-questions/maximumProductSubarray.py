def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    #assume first value is min/max product
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)): 
        num = nums[i]
        
        temp_max = max_product 
        max_product = max(num, max( temp_max * num, min_product * num )) 
        min_product = min(num, min( min_product * num, temp_max * num ))
        
        result = max(result, max_product)
        
    return result

if __name__ == '__main__': 
    print( maxProduct([2,3,-2,4]) )
            