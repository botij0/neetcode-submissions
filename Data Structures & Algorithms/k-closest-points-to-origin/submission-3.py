class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x,y = points[i]
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (d, i))
        
        result = []
        for _ in range(k):
            _, i = heapq.heappop(heap)
            result.append(points[i])
        
        return result
