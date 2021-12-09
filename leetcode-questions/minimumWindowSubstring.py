def minWindow( s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    
    # store result
    res = None
    
    # current counts
    counts = { }
    
    # initialize counts needed and starting counts
    countsNeeded = { }
    for char in t: 
        countsNeeded[char] = countsNeeded.get(char, 0) + 1
        counts[char] = 0
    
    # keep track if requirements are fulfilled
    have = 0
    need = len(set(list(t)))
    left = 0 
    right = 0 
    
    while right < len(s): 
        
        # check to increment current count 
        if s[right] in counts: 
            counts[s[right]] += 1
            if counts[s[right]] == countsNeeded[s[right]]:
                have += 1
                
        #print("checking: ", s[left: right + 1])
        #print("need: ", need, " have: ", have)
        #print("current counts: ", counts)      
        
        
        # remove the leftmost char
        # to shrink string
        while have == need: 
            
            #print("current string: ", s[left: right + 1])
            #print("have: " , have ," vs need: ", need)
            
            if res == None or len(res) > right - left + 1: 
                res = s[left: right + 1]

            popped_char = s[left]
            #print("popped char: ", popped_char)
            if popped_char in counts:
                counts[popped_char] -= 1 
                if counts[popped_char] < countsNeeded[popped_char]: 
                    have -= 1
            
            left += 1
            
        if have < need: 
            right += 1
            
    return res if res else ""



if __name__ == "__main__": 
    print( minWindow("ADOBECODEBANC", "ABC") )



