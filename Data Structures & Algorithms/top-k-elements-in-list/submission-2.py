class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        maxHeap = []
        for key, value in counter.items():
            heapq.heappush(maxHeap, (-value, key))
        
        r = []
        while k > 0:
            r.append(heapq.heappop(maxHeap)[1])
            k -= 1

        return r           
