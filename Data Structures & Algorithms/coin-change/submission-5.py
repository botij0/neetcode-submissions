class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for c in coins:
                if current_amount - c >= 0:
                    dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1