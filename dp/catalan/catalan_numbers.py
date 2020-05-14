import time


class Catalan:
    def catalan(self, n):
        if n <= 1:
            return 1
        res = 0
        for i in range(0, n):
            res += self.catalan(i) * self.catalan(n - i - 1)
        return res

    def memoized_catalan(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        res = 0
        for i in range(0, n):
            res += self.memoized_catalan(i, dp) * self.memoized_catalan(n - i - 1, dp)
        dp[n] = res
        return res


if __name__ == '__main__':
    start = time.time()
    # print(Catalan().catalan(15))
    end = time.time()
    print(end - start)
    start = time.time()
    print(Catalan().memoized_catalan(15, [-1] * 16))
    end = time.time()
    print(end - start)
