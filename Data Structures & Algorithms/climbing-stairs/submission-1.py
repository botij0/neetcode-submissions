class Solution:
    def climbStairs(self, n: int) -> int:
        def top_down(n:int, cache:dict)-> int:
            if n < 0:
                return 0
            elif 0 <= n < 2:
                return 1

            if n in cache:
                return cache[n]

            count = 0
            count += top_down(n-1, cache)
            count += top_down(n-2, cache)

            cache[n] = count

            return count

        def bottom_up(n:int) -> int:
            if n < 2:
                return n
            
            dp = [1, 1]
            i = 2
            while i <= n:
                tmp = dp[1]
                dp[1] = dp[0] + dp[1]
                dp[0] = tmp
                i += 1
            
            return dp[1]

        return bottom_up(n)
        # mem = {}
        # return top_down(n,mem)
        