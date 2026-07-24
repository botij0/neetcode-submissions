class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # cache = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        # return self.dfs(amount, coins, 0, cache)
        return self.dp(amount,coins)

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
    
    def dp(self, amount: int, coins: List[int]):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
