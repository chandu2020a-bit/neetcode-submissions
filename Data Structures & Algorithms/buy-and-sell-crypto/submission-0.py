class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j]-prices[i] >= 0 :
                    diff += [prices[j]-prices[i]]
        print(diff)
        return max(diff)
        