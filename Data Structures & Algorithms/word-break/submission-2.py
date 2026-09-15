class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.memoization(s, wordDict, {}, 0)
        return self.dp(s, wordDict)
    
    def dp(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1,-1):
            for w in wordDict:
                if i + len(w) > len(s):
                    continue
                
                if s[i : i + len(w)] != w:
                    continue
                
                dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]



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
