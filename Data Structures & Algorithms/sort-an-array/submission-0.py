class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)
    

    def mergeSort(self, nums: List[int], start: int, end: int) -> List[int]:
        if end - start + 1 <= 1:
            return nums
        
        mid = (start + end) // 2

        self.mergeSort(nums, start, mid)

        self.mergeSort(nums, mid+1, end)

        self.merge(nums, start, mid, end)

        return nums
    

    def merge(self, nums: List[int], start: int, mid: int, end:int):
        L = nums[start: mid + 1]
        R = nums[mid+1:end+1]

        i = 0
        j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1



        