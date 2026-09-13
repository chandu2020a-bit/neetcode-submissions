class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = -1
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j]-prices[i] >= diff :
                    diff = prices[j]-prices[i]
        
        return(diff)
        