class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        d = defaultdict(int)
        for i in range(len(nums2)):
            d[nums2[i]] = i
        
        for n in nums1:
            r.append(d[n])

        return r