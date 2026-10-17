class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.memoization(n, {}, 0)
        return self.dp(n)
    

    def dp(self, n: int):
        n0 = 1
        n1 = 1

        for i in range(2, n + 1):
            aux = n1
            n1 = n0 + n1
            n0 = aux
        
        return n1

    
    def memoization(self, n: int, memo: dict, i:int):
        if i > n:
            return 0

        if i in memo:
            return memo[i]
        
        if i == n:
            return 1
        
        memo[i] = self.memoization(n, memo, i+1) + self.memoization(n, memo, i+2)

        return memo[i]