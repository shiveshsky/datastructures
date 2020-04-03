class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        i=0
        j=len(B)-1
        if len(A)==1 or len(B)==1:
            return [A[0], B[0]]
        ans = [[99999999999, 99999999999]]
        max_diff = 999999999
        while i<len(A) and j>0:
            if A[i]+B[j]>C:
                if max_diff>abs(C-(A[i]+B[j])):
                    max_diff = abs(C-(A[i]+B[j]))
                    ans[0] = [i, j]
                if max_diff==abs(C-(A[i]+B[j])) and ans[0][0] >= i:
                    ans[0] = [i, j]
                j-=1
            elif A[i]+B[j]<C:
                if max_diff>abs(C-(A[i]+B[j])):
                    max_diff = abs(C-(A[i]+B[j]))
                    ans[0] = [i, j]
                if max_diff==abs(C-(A[i]+B[j])) and ans[0][0] >= i:
                    ans[0] = [i, j]
                i+=1
            elif A[i]+B[j]==C:
                return [A[i], B[j]]
        return A[ans[0][0]], B[ans[0][1]]


# print(Solution().solve([1,3,5,7,9], [ 2, 4, 6, 8, 10 ],  10))
print(Solution().solve([5,10,20], [1,2,30], 13))