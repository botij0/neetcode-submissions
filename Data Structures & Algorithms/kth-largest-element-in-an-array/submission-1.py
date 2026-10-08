class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x= heapq.nlargest(k, nums)
        return x[-1]