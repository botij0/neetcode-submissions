class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()

        while n not in cache:
            cache.add(n)
            n = self.aux(n)
            if n == 1:
                return True
        
        return False
    
    def aux(self, n: int):
        result = 0
        while n > 0:
            result += (n % 10)**2
            n = n//10
        return result