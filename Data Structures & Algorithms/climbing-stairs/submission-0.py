class Solution:
    def climbStairs(self, n: int) -> int:
        def memo(n:int, m:dict)-> int:
            if n < 0:
                return 0
            elif 0 <= n < 2:
                return 1

            if n in m:
                return m[n]

            c = 0
            c += memo(n-1,m)
            c += memo(n-2, m)

            m[n] = c

            return c

        mem = {}
        return memo(n,mem)
        