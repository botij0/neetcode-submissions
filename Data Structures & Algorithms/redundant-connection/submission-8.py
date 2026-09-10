class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

            visited = set()
            if self.dfs(adj, visited, src, -1):
                return [src, dst]
        
        return []

    def dfs(self, adj, visited: set, node:int, parent:int):
        if node in visited:
            return True
        
        visited.add(node)
        for neigh in adj[node]:
            if neigh == parent:
                continue
            
            if self.dfs(adj, visited, neigh, node):
                return True
        
        return False