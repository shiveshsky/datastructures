class Solution:
    def minimize(self, A, B, C):
        X=0
        Y=0
        Z=0
        diff = 9999999999
        while X<len(A) and Y<len(B) and Z<len(C):
            mini = min(A[X], min(B[Y], C[Z]))
            maxi = max(A[X], max(B[Y], C[Z]))
            diff = min(diff, maxi-mini)
            if diff==0: break
            if A[X] == mini: X+=1
            elif B[Y] == mini: Y+=1
            else: Z+=1
        return diff
print(Solution().minimize([1,4,10],[2,15,20],[10,12]))