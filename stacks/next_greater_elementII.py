from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2
        ans = [-1] * len(nums)
        stak = []
        for i in range(len(nums)):
            if not stak:
                stak.append(i)
            elif stak and nums[stak[-1]] > nums[i]:
                stak.append(i)
            else:
                while stak and nums[i] > nums[stak[-1]]:
                    p = stak.pop()
                    ans[p] = nums[i]
                stak.append(i)
        return ans[0:(len(nums) // 2)]


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
