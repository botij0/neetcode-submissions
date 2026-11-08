class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        result = 0
        for v in d.values():
            if v % 2 != 0:
                result += 1

        return True if result < 2 else False
        