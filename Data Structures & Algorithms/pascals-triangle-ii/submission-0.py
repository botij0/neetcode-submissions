class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        dp = [[] for _ in range(rowIndex)]
        dp[0] = [0,1,0]
        r = []
        for i in range(1,rowIndex):
            dp[i].append(0)
            for j in range(1, i + 2):
                dp[i].append(dp[i-1][j-1] + dp[i-1][j])
            dp[i].append(0)

        for j in range(1, rowIndex+2):
            r.append(dp[-1][j-1] + dp[-1][j])

        return r
