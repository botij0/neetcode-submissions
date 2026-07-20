class Solution:
    def arrangeCoins(self, n: int) -> int:
        L, R = 1, n
        r = 1
        while L <= R:
            rowGuess = (R + L) // 2
            guess = (rowGuess * (rowGuess + 1)) // 2

            if guess <= n:
                r = max(r,rowGuess)
                L = rowGuess + 1
            else:
                R = rowGuess - 1        

        return r