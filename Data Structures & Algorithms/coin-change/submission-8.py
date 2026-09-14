class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.memoization(coins, {}, amount)
        return -1 if result == 10001 else result
    
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