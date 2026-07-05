class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = n + 1
        
        m = 0
        for n in nums:
            current = n
            c = 1
            while d[current] in d:
                c += 1
                current = d[current]

            m = max(m,c)

        return m