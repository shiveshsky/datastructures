from math import sqrt, inf


class Solution:
    def countMinSquares(self, A):
        nums = [inf] * (A + 1)
        squares = []
        for i in range(1, int(sqrt(A))+1):
            nums[i*i] = 1
            squares.append(i*i)
        for i in range(1, A+1):
            for j in squares:
                if j <= i:
                    nums[i] = min(nums[i], nums[i-j]+1)
        return nums[-1]


if __name__ == '__main__':
    print(Solution().countMinSquares(100000))
