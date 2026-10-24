class Solution:
    def countBits(self, n: int) -> List[int]:
        result = deque()
        while n >= 0:
            curr = n
            r = 0
            while curr > 0:
                if curr & 1:
                    r += 1
                curr = curr >> 1
            result.appendleft(r)
            n -= 1
        return list(result)