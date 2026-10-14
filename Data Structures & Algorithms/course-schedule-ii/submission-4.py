class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        path = set()
        result = []

        for i in range(numCourses):
            if self.dfs(adj, visit, path, result, i):
                return []
        
        return result
    
    def dfs(self, adj: dict, visit: set, path: set, result: List[int], src: int):
        if src in path:
            return True
        
        if src in visit:
            return False
        
        path.add(src)
        visit.add(src)

        for neigh in adj[src]:
            if self.dfs(adj, visit, path, result, neigh):
                return True
            
        path.remove(src)
        result.append(src)
        return False