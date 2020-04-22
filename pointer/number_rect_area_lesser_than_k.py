class Solution:
    def solve(self, A, B):
        i=0
        j=len(A)-1
        cnt = 0
        mod = 10**9+7
        while i <= j:
            if A[i]*A[j] < B:
                cnt = ((2*(j-i)+1)%mod + cnt % mod)%mod
                i += 1
            else:
                j -= 1
        return cnt


if __name__ == '__main__':
    print(Solution().solve([1,2,3,4,5], 5))
#
# print(Solution().solve([5, 10, 20, 100, 105], 5))

