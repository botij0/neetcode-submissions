class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        result = 0
        while L < (len(prices) - 1):
            R = L + 1

            while R < len(prices) and prices[L] < prices[R]:
                result = max(result, prices[R]- prices[L])
                R += 1

            L = R

        return result
