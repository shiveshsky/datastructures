import math


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # max(3 max, 2 min and 1 max)
        ans = []
        max1 = -math.inf
        max2 = -math.inf
        max3 = -math.inf

        min1 = math.inf
        min2 = math.inf
        for ind, i in enumerate(A):
            if i<=min1:
                min2=min1
                min1=i
            elif i<=min2:
                min2=i
            if i>=max1:
                max3=max2
                max2=max1
                max1=i
            elif i>=max2:
                max3=max2
                max2=i
            elif i>=max3:
                max3=i
            if ind<2:
                ans.append(-1)
            else:
                max_prod = 1
                if max1 != -math.inf:
                    max_prod*=max1
                if max2 != -math.inf:
                    max_prod*=max2
                if max3 != -math.inf:
                    max_prod*=max3
                min_prod = 1
                if max1 != -math.inf:
                    min_prod *= max1
                if min1 != math.inf:
                    min_prod*= min1
                if min2 != math.inf:
                    min_prod *= min2
                ans.append(max((max_prod), (min_prod)))
        return ans

if __name__ == '__main__':
    print(Solution().solve( [ 11, 5, 6, 2, 8, 10 ]))
    print(Solution().solve([1, 2, 3, 4, 5]))
