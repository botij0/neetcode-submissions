class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()

        L = 0

        for n in nums:

            if len(s) > k:
                s.remove(nums[L])
                L += 1

            if n in s:
                return True
            
            s.add(n)

        return False