class Solution:
    def myPow(self, x: float, n: int) -> float:
        aux = x
        if n > 0:
            for i in range(n-1):
                x *= aux
            return x
        elif n == 0:
            return 1
        else:
            for i in range((-n)+1):
                x /= aux
                print(i)
            return x