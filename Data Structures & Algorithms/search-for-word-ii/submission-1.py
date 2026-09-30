class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Trie:
    def __init__ (self):
        self.root = TrieNode()
    
    def insert(self, word: str):
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

        result, cache = set(), set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, t.root, result, cache, i, j, "")

        return list(result)
        
    def dfs(self, board: List[List[str]], node: TrieNode, result: set, cache: set, i: int, j:int, word: str):
        if min(i, j) < 0 or i >= len(board) or j >= len(board[0]):
            return
        
        current = board[i][j]

        if current not in node.children or (i,j) in cache:
            return
        
        cache.add((i,j))
        node = node.children[current]
        word += current

        if node.word:
            result.add(word)

        self.dfs(board, node, result, cache, i+1, j, word)
        self.dfs(board, node, result, cache, i-1,j, word)
        self.dfs(board, node, result, cache, i,j+1, word)
        self.dfs(board, node, result, cache, i,j-1, word)

        cache.remove((i,j))











