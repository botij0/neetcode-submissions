class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        r = []
        for _ in range(numRows):
            dp.append([])
            r.append([])

        for i in range(numRows):
            dp[i].append(0)
            for j in range(1,i+2):
                if i < 2:
                    r[i].append(1)
                    dp[i].append(1)
                else:
                    dp[i].append(dp[i-1][j-1] + dp[i-1][j])
                    r[i].append(dp[i-1][j-1] + dp[i-1][j])

            dp[i].append(0)

        return r