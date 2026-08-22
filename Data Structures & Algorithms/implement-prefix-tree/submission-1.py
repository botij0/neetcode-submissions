class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        aux = self.root
        for c in word:
            if c not in aux.children:
                newNode = TrieNode()
                aux.children[c] = newNode

            aux = aux.children[c]
        
        aux.word = True


    def search(self, word: str) -> bool:
        aux = self.root
        for c in word:
            if c not in aux.children:
                return False
            aux = aux.children[c]
        
        return aux.word
        

    def startsWith(self, prefix: str) -> bool:
        aux = self.root
        for c in prefix:
            if c not in aux.children:
                return False
            
            aux = aux.children[c]
        return True
        
        