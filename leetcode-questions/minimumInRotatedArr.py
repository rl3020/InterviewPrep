def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    L, R =  0, len(nums) - 1
    
    while L < R: 
        
        #calculate mid value
        mid = (L + R) / 2
        
        # condition to find target value
        # all values are greater than the value that 
        # came before, EXCEPT the minimum value
        if mid > 0 and nums[mid] < nums[mid - 1]: 
            return nums[mid]
        
        # if the left side is sorted appropriately, 
        # then the answer must be in right side, so search right side
        elif nums[L] <= nums[mid] and nums[mid] > nums[R]:
            L = mid + 1
        
        # otherwise answer is in left side
        else: 
            R = mid - 1
            
        
    # return nums[L] because if we didn't find value in while loop, 
    # smallest value must be at the left pointer 
    return nums[L]



if __name__ == '__main__': 
    print( findMin([ 3,4,5,1,2 ]) )

