class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False] * (n + 1)

            if self.dfs(u, -1, visited, adj):
                return [u, v]
        
        return []

    
    def dfs(self, node:int, parent: int, visited: List[bool], adj: List[List[int]]):
        if visited[node]:
            return True
        
        visited[node] = True

        for new_node in adj[node]:
            if new_node == parent:
                continue
            
            if self.dfs(new_node, node, visited, adj):
                return True
        
        return False

            