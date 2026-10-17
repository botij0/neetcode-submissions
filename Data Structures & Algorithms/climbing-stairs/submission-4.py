class Solution:
    def climbStairs(self, n: int) -> int:
        return self.memoization(n, {}, 0)
    
    def memoization(self, n: int, memo: dict, i:int):
        if i > n:
            return 0

        if i in memo:
            return memo[i]
        
        if i == n:
            return 1
        
        memo[i] = self.memoization(n, memo, i+1) + self.memoization(n, memo, i+2)

        return memo[i]