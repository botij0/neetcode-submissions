class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return
        i = 0
        j = 0

        ptoInsert = m

        while j < n:
            while i < m and nums2[j] >= nums1[i]:
                i+=1;

            nums1.insert(i,nums2[j])
            nums1.pop()
            
            m+=1
            i = 0
            j+=1