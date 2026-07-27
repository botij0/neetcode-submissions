class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  
        return self.cycle_detection_dfs(edges)
          

    def cycle_detection_dfs(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

            visit = set()
            if self.dfs(src, -1, adjList, visit):
                return [src, dst]
        
        return []
    
    def dfs(self, node:int, parent:int, adjList: List[List[int]], visit: set):
        if node in visit:
            return True
        
        visit.add(node)
        for neighbor in adjList[node]:
            if neighbor == parent:
                continue

            if self.dfs(neighbor, node, adjList, visit):
                return True

        return False
