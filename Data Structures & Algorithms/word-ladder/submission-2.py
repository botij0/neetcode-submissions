class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neigh = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[1+j:]
                neigh[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[1+j:]
                    for neighbor in neigh[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            
            result += 1
        
        return 0