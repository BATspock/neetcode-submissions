class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        max_seen = prices[len(prices)-1]
        
        max_before = [0]*len(prices)

        for i in range(len(prices)-2, -1, -1):
            max_seen = max(max_seen, prices[i+1])
            max_before[i] = max_seen
        
        for i in range(len(prices)):
            profit = max(0, max(profit, max_before[i] - prices[i]))

        return profit