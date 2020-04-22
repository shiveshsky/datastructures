from heapq import heapify, heappush, heappop


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, K, A):
        ans = []
        minheap = []
        heapify(minheap)
        for i, num in enumerate(A):
            if len(minheap) < K:
                heappush(minheap, num)
            else:
                top = heappop(minheap)
                if num > top:
                    heappush(minheap, num)
                else:
                    heappush(minheap, top)
            if i<K-1:
                ans.append(-1)
            else:
                top = heappop(minheap)
                ans.append(top)
                heappush(minheap, top)
        return ans

if __name__ == '__main__':
    print(Solution().solve(4, [1,2,3,4,5,6]))