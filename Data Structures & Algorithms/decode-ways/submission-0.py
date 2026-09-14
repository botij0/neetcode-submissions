class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}
        return self.memoization(s, cache, 0)
    
    def memoization(self, s: str, cache: dict, i: int):
        if i in cache:
            return cache[i]
        
        if s[i] == "0":
            return 0

        result = self.memoization(s, cache, i + 1)
        if i + 1 < len(s) and (
            s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")
        ):
            result += self.memoization(s, cache, i + 2)

        cache[i] = result
        return cache[i]
