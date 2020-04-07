class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) and j<len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j=i+1
            while j<len(nums) and nums[j]==0:
                j+=1
            if i<len(nums) and j<len(nums):
                nums[i], nums[j] = nums[j], nums[i]



if __name__ == '__main__':
    A = [0,1,0,3,12]
    Solution().moveZeroes(A)
    print(A)
