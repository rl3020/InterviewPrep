def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    if len(prices) <= 1: 
        return 0
    
    buy = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)): 
        
        if buy > prices[i]: 
            buy = prices[i]
            
        elif prices[i] - buy > max_profit:
            max_profit = prices[i] - buy
            
    return max_profit


if __name__ == '__main__': 
    print( maxProfit([7,6,8,10,12]) )