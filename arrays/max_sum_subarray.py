class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = 0
        sum = 0
        i=0
        while i<len(nums):
            sum+=nums[i]
            max_sum = max(max_sum, sum)
        return max_sum
