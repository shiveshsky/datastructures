# class Solution:
#     def smallest_left(self, A):
#         stk = []
#         # ans = [i for i in range(0, len(A))]
#         ans = [0]*len(A)
#         for i in range(len(A)-1, -1, -1):
#             if len(stk) == 0:
#                 stk.append(i)
#             else:
#                 if A[stk[-1]] <= A[i]:
#                     stk.append(i)
#                 else:
#                     while len(stk) > 0 and A[stk[-1]] > A[i]:
#                         ind = stk.pop()
#                         ans[ind] = i+1
#                     stk.append(i)
#         return ans
#
#     def smallest_right(self, A):
#         stk = []
#         # ans = [i for i in range(0, len(A))]
#         ans = [len(A)-1]*len(A)
#         for i in range(0, len(A)):
#             if len(stk) == 0:
#                 stk.append(i)
#             else:
#                 if A[stk[-1]] <= A[i]:
#                     stk.append(i)
#                 else:
#                     while len(stk) > 0 and A[stk[-1]] > A[i]:
#                         ind = stk.pop()
#                         ans[ind] = i-1
#                     stk.append(i)
#         return ans
#
#     def largestRectangleArea(self, A):
#         left = self.smallest_left(A)
#         right = self.smallest_right(A)
#         if len(A)==1:
#             return A[0]
#         area = 0
#         for i in range(0, len(left)):
#             area = max(area, A[i]*(right[i] - left[i] + 1))
#
#
#         return area
#
#     def solve(self, A):
#         area = 0
#         height = []
#         for i in range(0, len(A)):
#             row = []
#             for j in range(0, len(A[0])):
#                 row.append(0)
#             height.append(row)
#
#         for i in range(0, len(A[0])):
#             for j in range(0, len(A)):
#                 if A[j][i]==0:
#                     continue
#                 else:
#                     if j==0:
#                         height[j][i]=1
#                     else:
#                         height[j][i]=height[j-1][i]+1
#         for row in height:
#             area = max(area, self.largestRectangleArea(row))
#         return area
class Solution:

    def smallest_left(self, A):

        stk = []

        # ans = [i for i in range(0, len(A))]

        ans = [0] * len(A)

        for i in range(len(A) - 1, -1, -1):

            if len(stk) == 0:

                stk.append(i)

            else:

                if A[stk[-1]] <= A[i]:

                    stk.append(i)

                else:

                    while len(stk) > 0 and A[stk[-1]] > A[i]:
                        ind = stk.pop()

                        ans[ind] = i + 1

                    stk.append(i)

        return ans

    def smallest_right(self, A):

        stk = []

        # ans = [i for i in range(0, len(A))]

        ans = [len(A) - 1] * len(A)

        for i in range(0, len(A)):

            if len(stk) == 0:

                stk.append(i)

            else:

                if A[stk[-1]] <= A[i]:

                    stk.append(i)

                else:

                    while len(stk) > 0 and A[stk[-1]] > A[i]:
                        ind = stk.pop()

                        ans[ind] = i - 1

                    stk.append(i)

        return ans

    def largestRectangleArea(self, A):

        left = self.smallest_left(A)

        right = self.smallest_right(A)

        if len(A) == 1:
            return A[0]

        area = 0

        for i in range(0, len(left)):
            area = max(area, A[i] * (right[i] - left[i] + 1))

        return area

    def max_area_histogram(self, histogram):

        stack = list()

        max_area = 0

        index = 0

        while index < len(histogram):

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):

                stack.append(index)

                index += 1

            else:

                top_of_stack = stack.pop()

                area = (histogram[top_of_stack] *

                        ((index - stack[-1] - 1)

                         if stack else index))

            max_area = max(max_area, area)

        while stack:

            top_of_stack = stack.pop()

            area = (histogram[top_of_stack] *

            ((index - stack[-1] - 1)

             if stack else index))

            max_area = max(max_area, area)

        return max_area

    def solve(self, A):

        area = 0

        for i in range(1, len(A)):

            for j in range(0, len(A[0])):

                if A[i][j] != 0:
                    A[i][j] += A[i - 1][j]

        for row in A:
            area = max(area, self.largestRectangleArea(row))

        return area
print(Solution().solve([  [0, 1, 0, 1],
                            [1, 0, 1, 0] ,
                              ]))

