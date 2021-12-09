
def coinChange( coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    cache = {}
    def getMinChange(coins, amount, count):
        
        if amount in cache: 
            return cache[amount]
        
        if amount == 0: 
            cache[amount] = count
            return count 
        
        if amount < 0: 
            cache[amount] = -1
            return -1
        
        results = [ ]
        for coin in coins: 
            results.append( getMinChange(coins, amount - coin, count) ) 
        
        
        results = [ value for value in results if value != -1 ]
        if results == [ ]: 
            cache[amount] = -1 
            return -1 
        else: 
            cache[amount] = min(results) + 1
            return cache[amount]
            
        
    
    return getMinChange(coins, amount, 0)
            
    
    
    