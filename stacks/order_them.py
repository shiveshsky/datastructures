class Solution:
    def solve(self, A):
        B = []
        C = []
        '''
            A->C
            C->B
            A->B
        '''
        expected = 1
        i=0
        while i<len(A):
            ele = A[i]
            if ele == expected:
                B.append(ele)
                expected +=1
                i+=1
            elif len(C)>0 and C[-1] == expected:
                B.append(C.pop())
                expected+=1
            else:
                C.append(ele)
                i+=1
        if len(C)>0:
            B = B+C[::-1]
        A.sort()
        return 1 if B == A else 0


print(Solution().solve([5,2,1,4,3]))
