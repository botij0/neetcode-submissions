class Solution:
    def climbStairs(self, n: int) -> int:
        result = []
        return self.dfs({}, n)

    def dfs(self, cache: dict, n:int):
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.dfs(cache, n-2) +  self.dfs(cache, n - 1)

        return cache[n]