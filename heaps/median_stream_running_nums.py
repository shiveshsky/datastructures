from heapq import heapify, heappush, heappop


class Solution:
    # @param A : list of integers
    # @return a list of integers

    def resize_heaps(self, minheap, maxheap):
        if abs(len(minheap)-len(maxheap)) > 1:
            if len(minheap)>len(maxheap):
                min_pop = heappop(minheap)
                heappush(maxheap, -1*min_pop)
            else:
                max_pop = heappop(maxheap)
                heappush(minheap, -1*max_pop)

    def solve(self, A):
        minheap = [] # for max elements (elements greater than median)
        maxheap = [] # for min elements (elements lesser than median)
        ans = []
        heapify(minheap)
        heapify(maxheap)
        heappush(minheap, A[0])
        median = A[0]
        ans.append(median)
        for num in A[1:]:
            if num < median:
                heappush(maxheap, -1*num)
                self.resize_heaps(minheap, maxheap)
            elif num >= median:
                heappush(minheap, num)
                self.resize_heaps(minheap, maxheap)
            if len(minheap) == len(maxheap):
                min_ele = heappop(minheap)
                max_ele = heappop(maxheap)
                median = -1*max_ele
                ans.append(median)
                heappush(minheap, min_ele)
                heappush(maxheap, max_ele)
            else:
                if len(minheap) < len(maxheap):
                    median = -1*heappop(maxheap)
                    ans.append(median)
                    heappush(maxheap, -1*median)
                else:
                    median = heappop(minheap)
                    ans.append(median)
                    heappush(minheap, median)
        return ans

if __name__ == '__main__':
    print(Solution().solve([5,17,100,11]))
    print(Solution().solve([1,2,3,4,5]))
    print(Solution().solve([59, 64, 10, 39 ]))