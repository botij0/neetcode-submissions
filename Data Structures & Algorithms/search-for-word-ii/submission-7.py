class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        aux = self.root
        for c in word:
            if c not in aux.children:
                aux.children[c] = TrieNode()
            
            aux = aux.children[c]
        aux.word = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for w in words:
            t.insert(w)

        result = set()
        cache = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, result, cache, i, j, t.root, "")

        return list(result)
    
    def dfs(self, board: List[List[str]], result: set, cache: set, i:int, j:int, node: TrieNode, current: str):
        if min(i,j) < 0 or i >= len(board) or j >= len(board[0]):
            return
        
        c = board[i][j]

        if (i,j) in cache or c not in node.children:
            return
        
        cache.add((i,j))
        current += c
        node = node.children[c]

        if node.word:
            result.add(current)
        
        self.dfs(board, result, cache, i+1, j, node, current)
        self.dfs(board, result, cache, i-1, j, node, current)
        self.dfs(board, result, cache, i, j+1, node, current)
        self.dfs(board, result, cache, i, j-1, node, current)

        cache.remove((i,j))






