class Solution:
    def solve(self, A, B):
            i=0
            j=len(A)-1
            cnt = 0
            mod = 10**9+7
            while i<j:
                if A[i]+A[j]<B:
                    i+=1
                elif A[i]+A[j]>B:
                    j-=1
                elif A[i]+A[j]==B:
                    cnt=(1+cnt)%mod
                    i+=1
            return cnt
# print(Solution().solve([1,2,3,4,5], 5))
# print(Solution().solve([5,10,20,100,105], 110))
# print(Solution().solve([1, 2, 2, 3, 4], 5))

