class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        result = []
        self.btrack(board, result, n, cols, posDiag, negDiag, 0)
        return result
    
    def btrack(self, board: List[List[str]], result: List[List[str]], n, cols: set, posDiag: set, negDiag: set, i: int):
        if i == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        
        for j in range(n):
            if j in cols or j+i in posDiag or i-j in negDiag:
                continue

            cols.add(j)
            posDiag.add(j+i)
            negDiag.add(i-j)

            board[i][j] = 'Q'
            self.btrack(board, result, n, cols, posDiag, negDiag, i + 1)
            board[i][j] = '.'
            cols.remove(j)
            posDiag.remove(i+j)
            negDiag.remove(i-j)








