class Solution:
    def solve(self, A, B):
        start = 0
        dek = []
        ans = []
        i = 0
        while i < len(A):
            if len(dek)==0 and A[i]<0:
                dek.append(i)
            else:
                if A[i] < 0:
                    dek.append(i)
            if i - start == B-1:
                if len(dek)>0 and start<=dek[0]<=i:
                    ans.append(dek[0])
                else:
                    ans.append(-99)
                    if len(dek)>0 and dek[0]<=start:
                        dek.pop(0)
                start += 1
                if len(dek)>0 and dek[0]<start:
                    dek.pop(0)
                # if start>dek[0]:
                    # dek.pop(0)
            i += 1
        return [A[i] if i>=0 else 0 for i in ans]


print(Solution().solve([ 4, 7, 5, 4, 4, 4, 0, 8, -10, -10, -6 ], 1))