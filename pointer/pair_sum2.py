class Solution:
    def solve(self, A, B):
            i = 0
            j = len(A)-1
            cnt = 0
            mod = 10**9+7
            while i < j:
                if A[i]+A[j] < B:
                    i += 1
                elif A[i]+A[j] > B:
                    j -= 1
                elif A[i]+A[j] == B:
                    x = A[i]
                    xx = i
                    while i < j and A[i] == x:
                        i += 1

                    # Find the frequency of A[j]
                    y = A[j]
                    yy = j
                    while j >= i and A[j] == y:
                        j -= 1

                    # If A[i] and A[j] are same
                    # then remove the extra number counted
                    if (x == y):
                        temp = i - xx + yy - j - 1
                        cnt += (temp * (temp + 1)) // 2
                    else:
                        cnt += (i - xx) * (yy - j)


            return cnt % mod


# print(Solution().solve([1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9], 2))
print(Solution().solve([1, 1, 1, 1, 1], 2))
# print(Solution().solve([1,2,3,3,4,6,7], 13)) # 1
# print(Solution().solve([1,2,2,3,4], 5)) # 3
# print(Solution().solve([2, 2, 3, 4, 4, 5, 6, 7, 10], 8)) # 4

