class Solve:
    '''
    TODO refer https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/
    '''

    def kadanes(self, arr, start, end):
        arrsum = arr[0]
        maxsum = arrsum[0]
        for i in range(1, len(arr)):
            arrsum += arr[i]
            if arrsum < 0:
                arrsum = 0
                start[0] = i
            if maxsum < arrsum:
                maxsum = arrsum
                start[0] = start[0]
                end[0] = i
        return maxsum

    def max_sum_submatrix(self, arr):
        start = [0]
        end = [0]
        global_sum = 0
        top_right_x = 0
        top_right_y = 0

        bottom_x = 0
        bottom_y = 0

        for i in range(0, len(arr[0])):
            temp = [0] * len(arr)
            for j in range(i, len(arr[0])):
                for t in range(i, j + 1):
                    temp[t] += arr[i][j]
                max_sum = self.kadanes(temp, start, end)

                if max_sum > global_sum:
                    global_sum = max_sum
                    top_right_x = i
                    top_right_y = j
                    bottom_x = start[0]
                    bottom_y = end[0]
        return (global_sum)


import math


class Solution:
    def kadens(self, arr, start, end):
        sum = 0
        maxsum = -math.inf
        end[0] = -1
        localstart = 0
        for i in range(0, len(arr)):
            sum += arr[i]
            if sum < 0:
                sum = 0
                localstart = i + 1
            if maxsum < sum:
                maxsum = sum
                start[0] = localstart
                end[0] = i
        if end[0] != -1:
            return maxsum
        # if all vals in arr are negative
        maxsum = arr[0]
        start[0] = end[0] = 0
        for i in range(1, len(arr)):
            if arr[i] > maxsum:
                maxsum = arr[i]
                start[0] = end[0] = i
        return maxsum

    def solve(self, A):
        overallsum = -math.inf
        for left in range(0, len(A[0])):
            tmp = [0] * len(A)
            for right in range(left, len(A[0])):
                for i in range(0, len(A)):
                    tmp[i] += A[i][right]
                maxsum_row = self.kadens(tmp, [0], [0])
                overallsum = max(overallsum, maxsum_row)
        return overallsum
