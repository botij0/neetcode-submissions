class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []

        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            # if nums[i] > 0:
            #     break

            p1, p2 = i + 1, len(nums) -1
            while p1 < p2:
                threeSum = nums[i] + nums[p1] + nums[p2]

                if threeSum == 0:
                    r.append([nums[i],nums[p1], nums[p2]])

                    p1 += 1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1 += 1

                elif threeSum > 0:
                    p2 -= 1
                else:
                    p1 += 1




        return r
