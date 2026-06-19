class Solution:
    def countBits(self, n: int) -> List[int]:
        r = [0 for i in range(n+1)]
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            
            r[i] = 1 + r[i-offset]

        return r