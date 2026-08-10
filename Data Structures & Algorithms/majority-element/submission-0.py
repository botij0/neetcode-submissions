class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        r = (-1, -1)
        for n in nums:
            counter[n] += 1
            if counter[n] > r[1]:
                r = (n, counter[n])
                
        return r[0]