class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        currSum = 0
        for n in nums:
            currSum += n
            self.sums.append(currSum)


    def sumRange(self, left: int, right: int) -> int:
        preRight = self.sums[right]
        preLeft = self.sums[left-1] if left > 0 else 0
        return preRight - preLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)