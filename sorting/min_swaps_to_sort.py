class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.count=0

    def solve(self, A):
        i=0
        cnt = 0
        while i<len(A):
            while A[i]!=i:
                tmp = A[i]
                A[i] = A[tmp]
                A[tmp] = tmp
                cnt+=1
            i+=1
        return cnt



print(Solution().solve([1,2,3,4,0]))
