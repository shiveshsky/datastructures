import math
from math import log2, ceil


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers

    def solve(self, A, B):
        height = (int)(ceil(log2(len(A))))
        max_size = 2 * (int)(2 ** height) - 1
        segment = [math.inf] * max_size
        self.create_segment_tree(A, 0, len(A) - 1, segment, 0)
        ans = []
        for row in B:
            if row[0] == 1:
                ans.append(
                    self.query_segment_tree(row[1]-1, row[2]-1, 0, len(A) - 1, 0, segment)
                )
            else:
                self.update(0, len(A) - 1, row[1]-1, row[2], segment, 0)
        return ans

    def create_segment_tree(self, A, start, end, segment, segment_ptr):
        if start == end:
            segment[segment_ptr] = A[start]
            return A[start]
        mid = (start + end) // 2

        segment[segment_ptr] = min(
            self.create_segment_tree(A, start, mid, segment, segment_ptr * 2 + 1),
            self.create_segment_tree(A, mid + 1, end, segment, segment_ptr * 2 + 2),
        )
        return segment[segment_ptr]

    def update(self, ss, se, ui, val, segment, sptr):
        if ui < ss or ui > se:
            return math.inf
        if ss == se and ss == ui:
            segment[sptr] = val
            return val
        mid = (ss + se) // 2

        self.update(ss, mid, ui, val, segment, sptr * 2 + 1),
        self.update(mid + 1, se, ui, val, segment, sptr * 2 + 2),

        segment[sptr] = min(segment[sptr*2+1], segment[sptr*2+2])
        return segment[sptr]

    def query_segment_tree(self, ql, qr, ss, se, sptr, segment):
        if ql <= ss and qr >= se:
            return segment[sptr]
        if se < ql or ss > qr:
            return math.inf
        mid = (ss + se) // 2
        return min(
            self.query_segment_tree(ql, qr, ss, mid, 2 * sptr + 1, segment),
            self.query_segment_tree(ql, qr, mid + 1, se, 2 * sptr + 2, segment),
        )


if __name__ == "__main__":
    # print(Solution().solve([1, 4, 1], [[1, 1, 3], [0, 1, 5], [1, 1, 2]]))
    print(Solution().solve([5, 4, 5, 7], [ [1, 2, 4], [0, 1, 2], [1, 1, 4]]))
