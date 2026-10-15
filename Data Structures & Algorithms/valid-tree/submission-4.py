class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()
        result = self.dfs(adj, visited, 0, 0)

        return result and len(visited) == n
    
    def dfs(self, adj: dict, visited: set, parent: int, node: int):
        if node in visited:
            return False
        
        visited.add(node)

        for neigh in adj[node]:
            if neigh == parent:
                continue
                
            if not self.dfs(adj, visited, node, neigh):
                return False

        return True
