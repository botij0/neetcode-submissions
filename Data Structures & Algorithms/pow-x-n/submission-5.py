class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
    
        return self.aux({}, x, n)

    def aux(self, cache: dict, x: float, n: int):
        if n == 0:
            return 1.0

        if n == 1:
            return x
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.aux(cache, x, n // 2) * self.aux(cache, x, n // 2 + n % 2)

        return cache[n]