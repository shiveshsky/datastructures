from heapq import heapify, heappush, heappop


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heap = []
        heapify(heap)
        for row in A:
            for i in row:
                if len(heap)<B:
                    heappush(heap, -1*i)
                else:
                    top = heappop(heap)
                    if -1*i > top:
                            heappush(heap, -1*i)
                    else:
                        heappush(heap, top)
        return -1*heappop(heap)

if __name__ == '__main__':
        print(Solution().solve(  [[5, 9, 11],
                [9, 11, 13],
                [10, 12, 15],
                [13, 14, 16],
                [16, 20, 21]], 12))
