class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        s = set()
        for i in range(min(nums), max(nums) + 1):
            s.add(i)
        
        for n in nums:
            if n not in s:
                return False
            s.remove(n)
        
        return True if len(s) == 0 else False