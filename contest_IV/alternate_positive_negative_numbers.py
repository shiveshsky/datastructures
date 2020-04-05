class Solution:
    def solve(self, A):
        # shifting all negative numbers to end
        i = 0
        end = len(A)-1
        while i<end:
            while A[i]>0:
                i+=1
            while A[end]<0:
                end-=1
            if i<end:
                tmp = A[i]
                A[i] = A[end]
                A[end] = tmp
        init = 0
        while init<len(A) and i<len(A):
            tmp = A[init]
            A[init] = A[i]
            A[i]=tmp
            i+=1
            init+=2
        return A

print(Solution().solve([-1,-2,-3,4,5]))