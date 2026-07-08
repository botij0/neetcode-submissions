class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        for n in nums1:
            r.append(nums2.index(n))
        return r