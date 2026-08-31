class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            r = x - y
            if r == 0:
                continue

            heapq.heappush(heap, -r)

        return -heap[0] if heap else 0