class Solution:
    def longestPalindrome(self, s: str) -> int:
        L = len(s)
        d = defaultdict(int)

        for c in s:
            d[c] += 1
        
        has_odd = False
        result = 0
        for v in d.values():
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                has_odd = True

        return result + 1 if has_odd else result