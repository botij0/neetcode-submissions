class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        return self.memoization(coins, amount, 0, cache)
    

    def memoization(self, coins: List[int], amount: int, i:int, cache: dict) -> int:
        if amount == 0:
            cache[(amount, i)] = 1
        elif amount < 0:
            cache[(amount, i)] = 0

        if i >= len(coins):
            cache[(amount, i)] = 0

        if (amount, i) in cache:
            return cache[amount, i]

        cache[(amount, i)] = (self.memoization(coins, amount - coins[i], i, cache) +
                self.memoization(coins, amount, i + 1, cache)
        )

        return cache[(amount, i)]