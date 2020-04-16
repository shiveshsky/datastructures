'''
Bob has an array A of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.

There are three types of operations that can be performed.

1 X -1: Update the value of A[X] to 2 * A[X] + 1.

2 X -1: Update the value A[X] to ⌊A[x]/2⌋ , where ⌊⌋ is Greatest Integer Function.

3 X Y: Take all the A[i] such that X <= i <= Y and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.

 A = 5
 B = [
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]
        [3, 1, 3]
        [3, 2, 4]
     ]
     [3, 2]
'''
from math import ceil, log2


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        height = (int)(ceil(log2(A)))
        segment_size = 2 * (int)(2 ** height) - 1
        segment = [0]*segment_size
        ans = []
        for row in B:
            if row[0]==1:
                self.update_incr(0, A-1, row[1]-1, segment, 0)
            elif row[0]==2:
                self.update_decr(0, A-1, row[1]-1, segment, 0)
            else:
                ans.append(self.query_segment_tree(row[1]-1, row[2]-1, 0, A - 1, 0, segment))
        return ans

    def update_incr(self, ss, se, ind, segment, sptr):
        if ind < ss or ind > se:
            return 0
        if ss == se and ss == ind:
            segment[sptr]+=1
            return segment[sptr]
        mid = (ss+se)//2
        self.update_incr(ss, mid, ind, segment, sptr * 2 + 1),
        self.update_incr(mid + 1, se, ind, segment, sptr * 2 + 2),
        segment[sptr] = segment[sptr * 2 + 1]+segment[sptr * 2 + 2]
        return segment[sptr]

    def update_decr(self, ss, se, ind, segment, sptr):
        if ind < ss or ind > se:
            return 0
        if ss == se and ss == ind:
            segment[sptr]-=1
            if segment[sptr]<0:
                segment[sptr] = 0
            return segment[sptr]
        mid = (ss+se)//2
        self.update_decr(ss, mid, ind, segment, sptr * 2 + 1),
        self.update_decr(mid + 1, se, ind, segment, sptr * 2 + 2),
        segment[sptr] = segment[sptr * 2 + 1]+segment[sptr * 2 + 2]
        return segment[sptr]

    def query_segment_tree(self, ql, qr, ss, se, sptr, segment):
        if ql <= ss and qr >= se:
            return segment[sptr]
        if se < ql or ss > qr:
            return 0
        mid = (ss + se) // 2
        return (self.query_segment_tree(ql, qr, ss, mid, 2 * sptr + 1, segment) +
            self.query_segment_tree(ql, qr, mid + 1, se, 2 * sptr + 2, segment))


if __name__ == '__main__':
    print(Solution().solve(5,
        [
            [1, 1, -1],
            [1, 2, -1],
            [3, 1, 3],
            [2, 1, -1],
            [3, 1, 3]
        ]
     ))