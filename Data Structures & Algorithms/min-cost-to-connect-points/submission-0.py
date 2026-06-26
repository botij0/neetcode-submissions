class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        
        for i in range(len(points)):
            adj[i] = []

        
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                adj[i].append([j, distance])
                adj[j].append([i, distance])


        minheap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, neighbor])
        
        mindistance = 0
        visit = set()
        visit.add(0)

        while len(visit) < len(points):
            weight, p1, p2 = heapq.heappop(minheap)
            
            if p2 in visit:
                continue
            
            mindistance += weight
            visit.add(p2)
            for neighbor, weight in adj[p2]:
                if neighbor not in visit:
                    heapq.heappush(minheap, [weight, p2, neighbor])
        
        return mindistance
        

                