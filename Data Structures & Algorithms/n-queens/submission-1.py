class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []

        col = set()
        posDiag = set()
        negDiag = set()
        self.btrack(board, result, col, posDiag, negDiag, n, 0)
        return result
    
    def btrack(self, board: List[List[str]], result: List[List[str]], col: set, posDiag: set, negDiag: set, n: int, i: int):

        if i == n:
            # append result
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        
        for j in range(n):
            if j in col or (i + j) in posDiag or (i - j) in negDiag:
                continue

            col.add(j)
            posDiag.add(i+j)
            negDiag.add(i-j)
            board[i][j] = 'Q'

            self.btrack(board, result, col, posDiag, negDiag, n, i+1)
            
            col.remove(j)
            posDiag.remove(i+j)
            negDiag.remove(i-j)
            board[i][j] = '.'