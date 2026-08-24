
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

    def insert(self, word: str):
        aux = self
        for c in word:
            if c not in aux.children:
                aux.children[c] = TrieNode()

            aux = aux.children[c]
        aux.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)
        
        res, visit = set(), set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, root, i, j, res, visit, "")

        return list(res)

    def dfs(self, board: List[List[str]], node: TrieNode, i:int, j:int, res:set, visit: set, word: str):
        if min(i,j) < 0 or i >= len(board) or j >= len(board[0]):
            return

        current = board[i][j]
        
        if current not in node.children or (i,j) in visit:
            return
        
        visit.add((i,j))
        node = node.children[current]
        word += current

        if node.word:
                res.add(word)


        self.dfs(board, node, i+1, j, res, visit, word)
        self.dfs(board, node, i-1, j, res, visit, word)
        self.dfs(board, node, i, j+1, res, visit, word)
        self.dfs(board, node, i, j-1, res, visit, word)

        visit.remove((i,j))

    


