class Solution:
    def prevSmaller(self, A):
        stk = []
        ans = [-1]*len(A)

        for i in range(len(A)-1, -1, -1):
            if len(stk)==0:
                stk.append(i)
            else:
                if A[stk[-1]]<=A[i]:
                    stk.append(i)
                else:
                    while len(stk)>0 and A[stk[-1]]>A[i]:
                        ind = stk.pop()
                        ans[ind] = A[i]
                    stk.append(i)

        return ans
if __name__ == '__main__':
    print(Solution().prevSmaller([4, 5, 2, 10, 8]))
    print(Solution().prevSmaller([34, 35, 27, 42, 5, 28, 39, 20, 28]))
