class LIS:
    def solve(self, A, num):
        if len(A) == 1 and num is None:
            return 1
        if len(A) < 1:
            return 1
        r1 = 0
        r2 = 0
        if num < A[0]:
            r1 = 1+self.solve(A[1:], A[0])
        else:
            r2 = max(self.solve(A[1:], A[0]), self.solve(A[1:], num))
        return max(r1, r2)

    def lis_bottom_up(self, arr):
        dp = [1]*(len(arr))
        for i in range(0, len(arr)):
            for j in range(i-1, -1, -1):
                if arr[i]>arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)



if __name__ == '__main__':
    print(LIS().solve([9, 2, 5, 3, 7, 101, 18], 10))