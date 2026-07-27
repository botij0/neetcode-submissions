class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.union_find_solution(edges)

    def dfs_solution(self, edges: List[List[int]]) -> List[int]:
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

    
    def union_find_solution(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node: int):
            p = parents[node]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(node_1: int, node_2: int):
            p1, p2 = find(node_1), find(node_2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True
        

        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return [node_1, node_2]
