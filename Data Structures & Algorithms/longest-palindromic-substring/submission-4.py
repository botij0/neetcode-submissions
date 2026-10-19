class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        result = ""

        for i in range(N -1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] ):
                    dp[i][j] = True
                    if len(result) < (j - i + 1):
                        result = s[i:j+1]
        
        return result