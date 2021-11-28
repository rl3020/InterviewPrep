def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0: 
        return 0 
    
    nums = set(nums)

    start_nodes = { }
    for num in nums: 
        next_val = num + 1
        prev_val = num - 1 
        
        if prev_val not in nums: 
            start_nodes[num] = []
            
            while next_val in nums: 
                start_nodes[num].append( next_val )
                next_val += 1
    
    all_lengths = []
    for start, neighbors in start_nodes.items(): 
        neighbors.append(start)
        all_lengths.append(len(neighbors)) 
        
    return max(all_lengths), start_nodes.keys(), start_nodes.values()

print( longestConsecutive([200, 4 , 100, 3, 1, 2]))


