class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)  == 0:
            return 0
                   
        cache = set()

        L = 0
        maxLength = 1

        for R in range(len(s)):
            c = s[R]
            if c in cache:
                while c in cache:
                    cache.remove(s[L])
                    L += 1
                
            maxLength = max(maxLength, R - L + 1)
            cache.add(c)

        return maxLength