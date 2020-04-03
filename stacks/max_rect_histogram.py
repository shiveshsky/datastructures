class Solution:
    def smallest_left(self, A):
        stk = []
        # ans = [i for i in range(0, len(A))]
        ans = [0]*len(A)
        for i in range(len(A)-1, -1, -1):
            if len(stk) == 0:
                stk.append(i)
            else:
                if A[stk[-1]] <= A[i]:
                    stk.append(i)
                else:
                    while len(stk) > 0 and A[stk[-1]] > A[i]:
                        ind = stk.pop()
                        ans[ind] = i+1
                    stk.append(i)
        return ans

    def smallest_right(self, A):
        stk = []
        # ans = [i for i in range(0, len(A))]
        ans = [len(A)-1]*len(A)
        for i in range(0, len(A)):
            if len(stk) == 0:
                stk.append(i)
            else:
                if A[stk[-1]] <= A[i]:
                    stk.append(i)
                else:
                    while len(stk) > 0 and A[stk[-1]] > A[i]:
                        ind = stk.pop()
                        ans[ind] = i-1
                    stk.append(i)
        return ans

    def largestRectangleArea(self, A):
        left = self.smallest_left(A)
        right = self.smallest_right(A)
        if len(A)==1:
            return A[0]
        area = 0
        for i in range(0, len(left)):
            area = max(area, A[i]*(right[i] - left[i] + 1))


        return area


print(Solution().largestRectangleArea([ 47, 69, 67, 97, 86, 34, 98, 16, 65, 95, 66, 69, 18, 1, 99, 56, 35, 9, 48, 72, 49, 47, 1, 72, 87, 52, 13, 23, 95, 55, 21, 92, 36, 88, 48, 39, 84, 16, 15, 65, 7, 58, 2, 21, 54, 2, 71, 92, 96, 100, 28, 31, 24, 10, 94, 5, 81, 80, 43, 35, 67, 33, 39, 81, 69, 12, 66, 87, 86, 11, 49, 94, 38, 44, 72, 44, 18, 97, 23, 11, 30, 72, 51, 61, 56, 41, 30, 71, 12, 44, 81, 43, 43, 27 ]))
print(Solution().largestRectangleArea([2,10,8])) # 16
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
print(Solution().largestRectangleArea([90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ])) # 348
