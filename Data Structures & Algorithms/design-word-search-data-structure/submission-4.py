class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        aux = self.root

        for c in word:
            if c not in aux.children:
                aux.children[c] = TrieNode()

            aux = aux.children[c]
        aux.word = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root, 0)
    
    def dfs(self, word: str, node: TrieNode, index: int):
        aux = node

        for i in range(index, len(word)):
            c = word[i]

            if c != '.' and c not in aux.children:
                return False
            
            if c == '.':
                for child in aux.children.values():
                    if self.dfs(word, child, i+1):
                        return True

                return False
   
            aux = aux.children[c]
        
        return aux.word
