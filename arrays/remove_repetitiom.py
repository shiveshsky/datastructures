class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = 0
        while j < len(nums) - 1:
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        if j < len(nums):
            nums[i] = nums[j]
            return i + 1
        else:
            return i


if __name__ == "__main__":
    print(Solution().removeDuplicates([2, 1, 1]))
