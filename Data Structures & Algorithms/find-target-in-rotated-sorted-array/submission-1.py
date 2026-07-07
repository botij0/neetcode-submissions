class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while nums[L] > nums [R]:
            if nums[R] == target:
                return R
            elif nums[L] == target:
                return L
            
            R -= 1
            L += 1
        
        # Binary Search
        while L <= R:
            mid = (L + R)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1
            
             