class Solution:
    def sqrt(self, A):
        l=1
        h=(A+1//2)
        ans = 1
        while l<=h:
            m = (l+h)//2
            square = m * m
            if square == A:
                return m
            elif square < A:
                l = m + 1
                ans = max(ans, m)
            elif square > A:
                h = m - 1
        return ans


if __name__ == '__main__':
    print(Solution().mySqrt(8))
