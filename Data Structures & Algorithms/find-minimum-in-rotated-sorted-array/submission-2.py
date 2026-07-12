class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        r = 0
        # 6 1 2 3 4 5
        # 1 2 3 4 5 6

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] > nums[-1]:
                L = mid + 1
            else:
                r = nums[mid]
                R = mid - 1
        
        return r
                
            