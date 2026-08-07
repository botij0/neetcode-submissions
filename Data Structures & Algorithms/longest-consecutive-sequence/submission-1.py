class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_numbers = set(nums)

        result = 0
        for n in nums:
            if n - 1 in unique_numbers:
                continue
            
            current = 1
            while n + current in unique_numbers:
                current += 1
            
            result = max(result, current)

        return result
            