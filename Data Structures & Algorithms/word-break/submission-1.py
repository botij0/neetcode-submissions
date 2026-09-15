class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.memoization(s, wordDict, {}, 0)
    
    def memoization(self, s: str, wordDict: List[str], cache: dict, i: int):
        if i == len(s):
            return True
            
        if i in cache:
            return cache[i]
        
        for w in wordDict:
            if i + len(w) > len(s):
                continue
            
            if s[i : i + len(w)] != w:
                continue
            
            if self.memoization(s, wordDict, cache, i + len(w)):
                cache[i] = True
                return cache[i]
        
        cache[i] = False
        return cache[i]
