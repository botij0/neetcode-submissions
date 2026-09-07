class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        path = set()

        for i in range(numCourses):
            if not self.dfs(adj, visit, path, i):
                return False
        
        return True
    
    def dfs(self, adj:dict, visit: set, path:set, src: int):
        if src in path:
            return False
        
        if src in visit:
            return True
        
        visit.add(src)
        path.add(src)

        for neighbor in adj[src]:
            if not self.dfs(adj, visit, path, neighbor):
                return False
        
        path.remove(src)
        return True