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
        def dfs(j, root):
            aux = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in aux.children.values():
                        if dfs(i+1, child):
                            return True

                    return False
                else:
                    if c not in aux.children:
                        return False
                    aux = aux.children[c]
            
            return aux.word

        return dfs(0, self.root)
