class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum =  nums[0]
        current_sum = 0
        for n in nums:
            current_sum = max(current_sum, 0) + n
            m_sum = max(m_sum, current_sum)

        return int(m_sum)
