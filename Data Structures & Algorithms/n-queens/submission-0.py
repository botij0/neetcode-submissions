class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []

        col = set()
        posDiag = set()
        negDiag = set()
        
        self.backtracking(result, board, n, col, posDiag, negDiag, 0)

        return result


    def backtracking(self, result: List[List[str]], board: List[List[str]], n:int, col: set, posDiag: set, negDiag: set, i: int):

        if i == n:
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

            self.backtracking(result, board, n, col, posDiag, negDiag, i+1)
            
            col.remove(j)
            posDiag.remove(i+j)
            negDiag.remove(i-j)
            board[i][j] = '.'
      