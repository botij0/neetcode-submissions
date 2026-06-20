class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for n in nums:
            if single == 0:
                single = n
            else:
                single ^= n

        return single