def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    
    nums_seen = {}
    for i, num in enumerate(nums): 
        if num not in nums_seen: 
            nums_seen[num] = i 
        else: 
            return True 
        
    return False

def containsDuplicate2(nums): 
    return not ( len(set(nums)) == len(nums) )

if __name__ == '__main__': 

    print( containsDuplicate([1,4,5,5,4,2,3,4,5,5,6,7]) ) 