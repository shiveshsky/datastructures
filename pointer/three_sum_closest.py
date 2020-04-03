class Solution:
    def threeSumClosest(self, A, B):
        A.sort()
        min_abs_diff = 999999999
        ans = 0
        for i in range(0, len(A)):
            j=i+1
            k=len(A)-1
            while k>j:
                temp = A[i]+A[j]+A[k]
                diff = abs(temp-B)
                if diff == 0:
                    return B
                if diff < min_abs_diff:
                    min_abs_diff = diff
                    ans=temp
                if temp<B:
                    j+=1
                else:
                    k-=1

        return ans
print(Solution().threeSumClosest([-1,2,1,-4], 1))


