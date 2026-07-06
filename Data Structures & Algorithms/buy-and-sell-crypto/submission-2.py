class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        m = 0
        for right in range(1,len(prices)):
            current = prices[right] - prices[left]
            
            if current <= 0:
                left = right
                continue
            
            m = max(m, current)
        
        return m
