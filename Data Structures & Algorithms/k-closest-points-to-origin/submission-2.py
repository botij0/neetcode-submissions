class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x1, x2 = points[i]
            d = math.sqrt(x1**2 + x2**2)
            heapq.heappush(heap, (d, i))

        result = []
        for d,i in heapq.nsmallest(k,heap):
            result.append(points[i])

        return result