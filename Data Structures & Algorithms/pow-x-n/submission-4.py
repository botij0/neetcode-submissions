class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.aux(x, -n)
        
        return self.aux(x, n)

        return r
    def aux(self, x: float, n:int) -> float:
        if n == 1:
            return x

        return self.myPow(x, n//2) * self.myPow(x, n//2 + n%2)