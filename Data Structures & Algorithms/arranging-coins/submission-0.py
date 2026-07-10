class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n > 0:
            n -= i
            i += 1
        
        if n < 0:
            return i - 2
        else:
            return i -1
