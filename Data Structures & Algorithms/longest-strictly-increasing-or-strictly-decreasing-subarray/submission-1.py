class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mInc = 1
        currInc = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                mInc = max(mInc, currInc)
                currInc = 1
                continue
            currInc += 1
        mInc = max(mInc, currInc)    

        mDec = 1
        currDec = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                mDec = max(mDec, currDec)
                currDec = 1
                continue
            currDec += 1
        mDec = max(mDec, currDec)

        return max(mInc, mDec)
