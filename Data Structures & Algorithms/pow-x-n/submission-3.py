class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        aux = x
        negative = n < 0

        if negative:
            n *= -1

        i = 1
        while i < n:
            x *= aux
            i += 1

        return x if not negative else 1/x