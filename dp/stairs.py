class Solution:
    # allowed steps are 1, 2
    def climbStairs(self, A):
        stairs = [0]*A
        stairs[0] = 1
        if len(stairs)>1:
            stairs[1] = 2
        i = 2
        while i < len(stairs):
            stairs[i] = stairs[i-1]+stairs[i-2]
            i += 1
        return stairs[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(36))