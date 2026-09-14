class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # result = self.memoization(coins, {}, amount)
        # return -1 if result == 10001 else result
        return self.dp(coins, amount)
    
    def dp(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for currAmount in range(1, amount + 1):
            for c in coins:
                if currAmount - c >= 0:
                    dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

    
    def memoization(self, coins: List[int], cache: dict, currentAmount: int):
        if currentAmount == 0:
            return 0

        if currentAmount in cache:
            return cache[currentAmount]

        result = 10001
        for coin in coins:
            if currentAmount - coin >= 0:
                result = min(result, 1 + self.memoization(coins, cache, currentAmount - coin))

        cache[currentAmount] = result
        return cache[currentAmount]