"""
Problem Description
Given an integer A denoting the size of the array consisting all ones. You are given Q queries, for each query there are two integer x and y:
If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: Your Solution may run on multiple test cases. NOTE 2: There will atleast 1 query where value of x is 1.
"""

from math import ceil, log2


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        height = (int)(ceil(log2(A)))
        # segment_size = 2 * (int)(2 ** height) - 1
        segment_size = 4 * A
        segment = [0] * segment_size
        ans = []
        self.create_segment_tree(0, A - 1, segment, 0)
        for row in B:
            if row[0] == 0:
                self.update_tree(0, A - 1, row[1] - 1, segment, 0)
            else:
                ans.append(self.query_segment_tree(0, A - 1, 0, segment, row[1]))
        return ans

    def update_tree(self, ss, se, ind, segment, sptr):
        if ind < ss or ind > se:
            return 0
        if ss == se and ss == ind:
            segment[sptr] = 0
            return -1
        mid = (ss + se) // 2
        self.update_tree(ss, mid, ind, segment, sptr * 2 + 1),
        self.update_tree(mid + 1, se, ind, segment, sptr * 2 + 2),
        segment[sptr] = segment[sptr * 2 + 1] + segment[sptr * 2 + 2]
        return segment[sptr]

    def create_segment_tree(self, start, end, segment, segment_ptr):
        if start == end:
            segment[segment_ptr] = 1
            return 1
        mid = (start + end) // 2

        segment[segment_ptr] = self.create_segment_tree(
            start, mid, segment, segment_ptr * 2 + 1
        ) + self.create_segment_tree(mid + 1, end, segment, segment_ptr * 2 + 2)
        return segment[segment_ptr]

    def query_segment_tree(self, ss, se, sptr, segment, val):
        if val > segment[sptr]:
            return -1
        if ss == se:
            return se+1
        mid = (ss+se)//2
        leftindex = 2*sptr+1
        rightindex = 2*sptr+2

        if val<=segment[leftindex]:
            return self.query_segment_tree(ss, mid, leftindex, segment, val)
        else:
            leftcount = segment[leftindex]
            return self.query_segment_tree(mid+1, se, rightindex, segment, val-leftcount)
        return -1

    # def query_segment_tree(self, ss, se, sptr, segment, val):
    #     if val == segment[sptr]:
    #         if segment[sptr * 2 + 2] > 0:
    #             return se + 1
    #     mid = (ss + se) // 2
    #     if 2 * sptr >= len(segment):
    #         return -1
    #     left = segment[2 * sptr + 1]
    #     if left < val:
    #         right_val = self.query_segment_tree(
    #             mid + 1, se, 2 * sptr + 2, segment, val - left
    #         )
    #         if right_val != -1:
    #             return right_val
    #     else:
    #         left_val = self.query_segment_tree(ss, mid, 2 * sptr + 1, segment, val)
    #         if left_val != -1:
    #             return left_val
    #     return -1


if __name__ == "__main__":
    print(
        Solution().solve(
            13,
            [[0, 7], [1, 8], [0, 5], [0, 12], [1, 1], [1, 6], [1, 11], [1, 9], [1, 3]],
        )
    )
