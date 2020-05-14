class Solution:
    def chordCnt(self, A):
        n = 2 * A
        # dp array containing the sum
        dpArray = [0]*(n + 1)
        dpArray[0] = 1
        dpArray[2] = 1
        mod = 10**9 + 7
        for i in range(4, n + 1, 2):
            for j in range(0, i-1, 2):
                dpArray[i] = ((dpArray[j]*dpArray[i-2-j]) % mod + (dpArray[i]) % mod) % mod
        return int(dpArray[n]) % mod

if __name__ == '__main__':
    print(Solution().chordCnt(3))