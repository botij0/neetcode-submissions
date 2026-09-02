class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        coundict = defaultdict(int)
        for t in tasks:
            coundict[t] += 1
        
        heap = [ -cnt for cnt in coundict.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)  # -heapq.heappop(heap) - 1
                if cnt != 0:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time