import math


class Solution:
    def solve(self, A):
        A.sort()
        ans = math.inf
        for i in range(0, len(A)):
            for k in range(i+1, len(A)):
                tmparr = [A[j] for j in range(0, len(A)) if (j!=i and j!=k)]
                sum_odd = sum([tmparr[l] for l in range(0, len(tmparr), 2)])
                sum_even = sum([tmparr[l] for l in range(1, len(tmparr), 2)])
                ans = min(ans, abs(sum_odd-sum_even))
        return ans


if __name__ == '__main__':
    print(Solution().solve([81, 19, 42, 70, 79, 56, 38, 106, 59, 47, 16, 65, 93, 34, 112, 37, 57, 29, 114, 107]))
    print(Solution().solve([2, 4, 1, 10, 6, 15]))
