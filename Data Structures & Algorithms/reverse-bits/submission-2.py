class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        i = 0
        while n > 0:
            if n & 1:
                r += 1 * math.pow(2, 31 - i)
            i += 1
            n = n // 2

        return int(r)