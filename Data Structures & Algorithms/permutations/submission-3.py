class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            currPerm = []
            for p in result:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    currPerm.append(copy)

            result = currPerm

        return result
    
    # def btrack(self, nums: List[int], result: List[List[int]], i:int, current: List[int]):
    #     if i >= len(nums):
