class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        x = str(math.log2(n))
        return x.split('.')[-1] == '0'