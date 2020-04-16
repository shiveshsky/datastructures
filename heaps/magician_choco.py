import heapq
from heapq import heapify, heappop
from math import floor


class Solution:
    def nchoc(self, A, B):
        min_B = [-1*i for i in B]
        heapify(min_B)
        sum = 0
        mod = (10**9) + 7
        for i in range(0, A):
            choco = heappop(min_B)
            heapq.heappush(min_B, -1*floor((-1*choco)/2.0))
            sum = (sum%mod + (-1*choco)%mod)
        return sum%mod
if __name__ == '__main__':
    print(Solution().nchoc(3, [6,5]))