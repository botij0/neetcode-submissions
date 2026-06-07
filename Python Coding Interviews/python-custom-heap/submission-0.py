import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    r = []
    
    for n in nums:
        pair = (-n, n)
        heapq.heappush(max_heap, pair)
    
    while max_heap:
        i,n = heapq.heappop(max_heap)
        r.append(n)
    
    return r



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
