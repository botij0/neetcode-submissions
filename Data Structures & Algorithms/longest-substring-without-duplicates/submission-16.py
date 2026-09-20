class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        L = 0
        result = 1
        current = set(s[L])
        for R in range(1, len(s)):
            if s[R] not in current:
                current.add(s[R])
                result = max(result, R-L + 1)
                continue
            
            while s[R] in current:
                current.remove(s[L])
                L += 1

            current.add(s[R])
            
        return result

        