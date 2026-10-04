class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                cache = set()
                if self.btrack(board, word,cache, i, j, 0):
                    return True
        return False     
    
    def btrack(self, board: List[List[str]], word: str, cache: set, i: int, j:int, curr:int):
        if min(i,j) < 0 or i >= len(board) or j >= len(board[0]):
            return False
        
        if word[curr] != board[i][j] or (i,j) in cache:
            return False
        
        if word[curr] == board[i][j] and curr == len(word) - 1:
            return True
        
        cache.add((i,j))
        curr += 1

        result = (
            self.btrack(board, word, cache, i + 1, j, curr) or
            self.btrack(board, word, cache, i - 1, j, curr) or
            self.btrack(board, word, cache, i, j + 1, curr) or
            self.btrack(board, word, cache, i, j - 1, curr)
        )

        cache.remove((i,j))
        return result