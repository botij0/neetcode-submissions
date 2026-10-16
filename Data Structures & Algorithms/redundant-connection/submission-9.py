class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

            if self.dfs(adj, set(), -1, src):
                return [src, dst]
        
        return []
    
    def dfs(self, adj: dict, visited: set, parent: int, node: int):
        if node in visited:
            return True
        
        visited.add(node)

        for neigh in adj[node]:
            if neigh == parent:
                continue

            if self.dfs(adj, visited, node, neigh):
                return True
        
        return False
