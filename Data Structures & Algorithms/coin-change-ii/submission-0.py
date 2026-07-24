class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        return self.dfs(amount, coins, 0, cache)

    def dfs(self, amount: int, coins: List[int], i: int, cache) -> int:
        if i >= len(coins):
            return 0
        
        if amount == 0:
            return 1

        elif amount < 0:
            return 0
        
        if cache[i][amount] != -1:
            return cache[i][amount]
      
        cache[i][amount] = (self.dfs(amount - coins[i], coins, i, cache) + 
                self.dfs(amount, coins, i+1, cache)
        )

        return cache[i][amount]
