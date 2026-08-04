class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()

        L = len(nums1)
        m = L//2
        if L % 2 == 1:
            return float(nums1[m])
        else:
            return (nums1[m] + nums1[m-1])/2