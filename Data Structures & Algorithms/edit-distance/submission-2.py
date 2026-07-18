class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1 = len(word1)
        L2 = len(word2)

        cache = {}

        return self.dfs(word1, word2, 0, 0, L1, L2, cache)
        
    def dfs(self, word1, word2, i, j, L1, L2, cache):
        if i == L1:
            return L2 - j
        
        if j == L2:
            return L1 - i

        if (i,j) in cache:
            return cache[(i,j)]

        if word1[i] == word2[j]:
            cache[(i,j)] = self.dfs(word1, word2, i+1,j+1, L1, L2, cache)
        else:
            cache[(i,j)] = 1 + min(
                self.dfs(word1, word2, i+1, j, L1, L2, cache),
                self.dfs(word1, word2, i, j+1, L1, L2, cache),
                self.dfs(word1, word2, i+1, j+1, L1, L2, cache)
            )

        return cache[(i,j)]
        


