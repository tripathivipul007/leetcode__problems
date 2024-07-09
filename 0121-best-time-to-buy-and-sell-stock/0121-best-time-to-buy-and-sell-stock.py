class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minprice = prices[0]
        maxprofit =0
        
        for price in prices:
            if price < minprice:
                minprice = price
                
            elif price-minprice > maxprofit:
                    maxprofit = price-minprice
                    
        return maxprofit