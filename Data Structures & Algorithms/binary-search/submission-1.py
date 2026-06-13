class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = int((left+right)/2)
            n = nums[middle]

            if target > n:
                left = middle + 1
            elif target < n:
                right = middle -1
            else:
                return middle
        
        return -1