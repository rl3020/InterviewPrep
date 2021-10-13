def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    values_seen = {}
    found = False
    result = []
    for i, number in enumerate(nums): 
        complement =  target - number 
        
        if complement in values_seen: 
            found = True
            result = [values_seen[complement], i]
            break 
        else: 
            
            values_seen[number] = i
            
    return result


if __name__ == "__main__": 
    print( twoSum([1,2,3,4,5] , 9) )

    