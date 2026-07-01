class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux = defaultdict(int)

        for n in nums:
            aux[n] += 1
        
        r = []
        max_heap = []

        for key, value in aux.items():
            heapq.heappush(max_heap, (-value, key))
        
        for _ in range(k):
            c, val = heapq.heappop(max_heap)
            r.append(val)
        
        return r