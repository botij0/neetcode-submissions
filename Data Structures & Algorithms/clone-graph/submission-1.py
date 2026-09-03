"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})
    
    def bfs(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)

        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                oldToNew[curr].neighbors.append(oldToNew[neighbor])


        return oldToNew[node]
    
    def dfs(self, node: Optional['Node'], oldToNew: dict):
        if not node:
            return
        
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor, oldToNew))
        
        return copy
        
        
