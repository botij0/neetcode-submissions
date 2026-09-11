class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.dfs({}, n)
        return self.dp(n)

    def dp(self, n: int):
        if n < 2:
            return 1
        
        current_step = 1
        previous_step = 1

        for _ in range(n-1):
            temp = current_step
            current_step = previous_step + current_step
            previous_step = temp
        
        return current_step
            


    def dfs(self, cache: dict, n:int):
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.dfs(cache, n-2) +  self.dfs(cache, n - 1)

        return cache[n]
    

