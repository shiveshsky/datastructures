from heapq import heapify, heappop, heappush


class Solution:
    def solve(self, A, B, C):
        maxships = C.copy()
        maxships = [-1*i for i in maxships]
        heapify(maxships)
        minships = C.copy()
        heapify(minships)
        maxmoney = 0
        minmoney = 0

        maxB = 0
        while maxB<A:
            top=-1*heappop(maxships)
            heappush(maxships, -1*(top-1))
            maxmoney += top
            maxB+=1
        minB = 0
        while minB<A:
            top = heappop(minships)
            if top-1>0:
                heappush(minships, top-1)
            minmoney+= top
            minB+=1
        return [maxmoney, minmoney]


if __name__ == '__main__':
    print(Solution().solve(4, 3, [2, 2, 2]))
