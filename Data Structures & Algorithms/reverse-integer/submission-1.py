class Solution:
    def reverse(self, x: int) -> int:
        signed = x < 0
        aux =  int(str(abs(x))[::-1])
        result = aux if not signed else -aux

        return result if -2**31 <= result <= 2**31 - 1 else 0