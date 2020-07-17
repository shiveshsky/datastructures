class Solution:
    def searchRange(self, nums, target):
        l, r = (self.left_position([5, 7, 7, 8, 8, 10], 6), self.right_position([5, 7, 7, 8, 8, 10], 6))
        return [l, r]

    def left_position(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                    r -= 1
                else:
                    return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def right_position(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid + 1 >= 0 and nums[mid + 1] == nums[mid]:
                    l += 1
                else:
                    return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().searchRange(None, None))
