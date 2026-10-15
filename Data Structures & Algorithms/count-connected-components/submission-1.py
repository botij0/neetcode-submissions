class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        result = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            result += 1
            self.dfs(adj, visited, i)
        
        return result
    
    def dfs(self, adj: dict, visited: set, node: int):
        if node in visited:
            return
        
        visited.add(node)

        for neigh in adj[node]:
            self.dfs(adj, visited, neigh)
        