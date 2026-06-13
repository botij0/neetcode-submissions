class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            r = self.binarySearch(l, target)
            if r != -1:
                return True
        
        return False
    

    def binarySearch(self,nums:List[int], target:int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = int((left+right)/2)
            n = nums[middle]

            if n == target:
                return middle
            elif n > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1