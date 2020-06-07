class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        max_seen_so_far = A[0]
        i = 1
        cnt = 0
        while i < len(A):
            if A[i] == max_seen_so_far:
                A[i] += 1
                cnt += 1
            elif A[i] < max_seen_so_far:
                cnt += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1

                # while A[i] <= max_seen_so_far:
                #     A[i] += 1
                #     cnt += 1

            max_seen_so_far = max(max_seen_so_far, A[i])
            i += 1
        return cnt


if __name__ == '__main__':
    print(Solution().solve([2, 3, 3, 4, 4, 5]))
    # print(Solution().solve([1,1,3]))

    # print(Solution().solve([ 51, 6, 10, 8, 22, 61, 56, 48, 88, 85, 21, 98, 81, 76, 71, 68, 18, 6, 14, 23, 72, 18, 56, 30, 97, 100, 81, 5, 99, 2, 85, 67, 46, 32, 66, 51, 76, 53, 36, 31, 81, 56, 26, 75, 69, 54, 54, 54, 83, 41, 86, 48, 7, 32, 85, 23, 47, 23, 18, 45, 79, 95, 73, 15, 55, 16, 66, 73, 13, 85, 14, 80, 39, 92, 66, 20, 22, 25, 34, 14, 51, 14, 17, 10, 100, 35, 9, 83, 31, 60, 24, 37, 69, 62 ]))
    # print(Solution().solve([1, 1, 1, 20, 20, 30]))
