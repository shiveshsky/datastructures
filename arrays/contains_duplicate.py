class Solution:
    def containsDuplicate(self, nums) -> bool:
        return not len(set(nums)) == len(nums)
