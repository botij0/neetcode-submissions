class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue

                if self.dfs(board, i, j, word, 0):
                    return True

        return False

    def dfs(self, board: List[List[str]], i: int, j: int, word: str, target: int):
        if min(i,j) < 0 or i >= len(board) or j>=len(board[0]):
            return False
        
        if board[i][j] != word[target]:
            return False
        
        if target == len(word) - 1:
            return True
        
        temp = board[i][j]
        board[i][j] = '#'

        found = (
            self.dfs(board, i + 1, j, word, target + 1) or
            self.dfs(board, i - 1, j, word, target + 1) or
            self.dfs(board, i, j + 1, word, target + 1) or
            self.dfs(board, i, j - 1, word, target + 1)
        )

        board[i][j] = temp
        return found


