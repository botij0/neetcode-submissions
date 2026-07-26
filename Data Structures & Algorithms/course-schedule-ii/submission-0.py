class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        path = set()

        for i in range(numCourses):
            if not self.dfs(i, adj, visited, path):
                return []
        
        path_list = []
        visited = set()

        for i in range(numCourses):
            self.build_path(i, adj, visited, path_list)
        
        return path_list
    
    def build_path(self, src: int, adj: dict, visited: set, path_list: List[int]):
        if src in visited:
            return
        
        visited.add(src)

        for neighbor in adj[src]:
            self.build_path(neighbor, adj, visited, path_list)

        path_list.append(src)

    
    def dfs(self, src: int, adj: dict, visited: set, path: set):
        if src in path:
            return False
        
        if src in visited:
            return True
        
        visited.add(src)
        path.add(src)

        for neighbor in adj[src]:
            if not self.dfs(neighbor, adj, visited, path):
                return False
        
        path.remove(src)
        return True