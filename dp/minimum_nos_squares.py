from math import sqrt, inf


class Solution:
    def countMinSquares(self, A):
        nums = [inf] * (A + 1)
        squares = []
        for i in range(1, int(sqrt(A)) + 1):
            nums[i * i] = 1
            squares.append(i * i)
        for i in range(1, A + 1):
            for j in squares:
                if j <= i:
                    nums[i] = min(nums[i], nums[i - j] + 1)
        return nums[-1]

    def recc(self, A):
        # TODO memoize take a dp array and if A is there return directly
        # else put ans in A in dp array
        if A == 0:
            return 0
        if A == 1:
            return 1
        ans = 9999999999
        for i in range(int(sqrt(A)), 0, -1):
            ans = min(1 + self.recc(A - (i ** 2)), ans)
        return ans


if __name__ == '__main__':
    print(Solution().recc(5))
    # print(Solution().countMinSquares(100000))
