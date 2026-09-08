class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        path = set()
        current = []

        for n in range(numCourses):
            if not self.dfs(adj, visited, path, n, current):
                return []
            
        return current

    
    def dfs(self, adj:dict, visited: set, path: set, src: int, current: List[int]):
        if src in path:
            return False
        
        if src in visited:
            return True

        visited.add(src)
        path.add(src)

        for neig in adj[src]:
            if not self.dfs(adj, visited, path, neig, current):
                return False
        
        path.remove(src)
        current.append(src)
        return True