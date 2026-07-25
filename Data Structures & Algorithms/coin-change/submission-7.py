class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for target_amount in range(1, len(dp)):
            for c in coins:
                if target_amount - c >= 0:
                    dp[target_amount] = min(dp[target_amount], 1 + dp[target_amount - c])

        return dp[-1] if dp[-1] != amount + 1 else -1