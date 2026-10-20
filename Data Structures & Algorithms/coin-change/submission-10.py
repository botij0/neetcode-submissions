class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.memoization(coins, {}, amount)
        if result == 10001:
            return -1
        return result
        # return self.dp(coins, amount)
    
    def dp(self, coins: List[int], amount: int):
        return 0
    
    def memoization(self, coins: List[int], cache: dict, amount: int):
        if amount == 0:
            return 0

        if amount in cache:
            return cache[amount]
        
        result = 10001
        for coin in coins:
            if amount - coin >= 0:
                result = min(result, 1 + self.memoization(coins, cache, amount - coin))
        
        cache[amount] = result
        return cache[amount]