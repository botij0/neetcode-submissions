class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.comps = n
    
        for i in range(n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        self.comps -= 1
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = UnionFind(n)
        for u, v in edges:
            if not dsu.union(u,v):
                return False
        
        return dsu.comps == 1


        
