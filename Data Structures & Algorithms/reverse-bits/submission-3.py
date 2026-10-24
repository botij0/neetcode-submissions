class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n & (1 << i):
                result += math.pow(2, 31-i)

        return int(result)