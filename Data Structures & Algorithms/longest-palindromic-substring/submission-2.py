class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.dp(s)
    
    def dp(self, s: str) -> str:
        resultIndex, resultLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resultLen < (j - i + 1):
                        resultIndex = i
                        resultLen = j - i + 1
        
        return s[resultIndex : resultIndex + resultLen]