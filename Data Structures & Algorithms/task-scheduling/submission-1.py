class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [ -cnt for cnt in c.values()]
        heapq.heapify(heap)

        result = 0
        queue = deque()

        while queue or heap:
            if heap:
                inst = heapq.heappop(heap) + 1
                if inst != 0:
                    queue.append((result + n, inst))

            while queue and queue[0][0] == result:
                curr = queue.popleft()
                heapq.heappush(heap, curr[1])


            result += 1

        return result