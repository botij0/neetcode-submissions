class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_p, fast_p = 0, 0

        while True:
            slow_p = nums[slow_p]
            fast_p = nums[nums[fast_p]]

            if slow_p == fast_p:
                break
        
        slow2_p = 0
        
        while True:
            slow_p = nums[slow_p]
            slow2_p = nums[slow2_p]

            if slow2_p == slow_p:
                break

        return slow2_p