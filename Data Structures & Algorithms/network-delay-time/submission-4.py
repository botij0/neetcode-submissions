class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for u, v, t in times:
            adj[u].append([v, t])
        
        shortest = {}
        min_heap = [[0, k]]

        while min_heap:
            t1, v1 = heapq.heappop(min_heap)
            
            if v1 in shortest:
                continue

            shortest[v1] = t1

            for v2, t2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(min_heap, [t1 + t2, v2])
        
        r = 0
        for i in range(1, n+1):
            if i not in shortest:
                return -1

            r = max(r, shortest[i])

        return r
