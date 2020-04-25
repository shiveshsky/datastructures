class Solution:
    def adjacent(self, A):
        ans = [0] * (len(A[0]))
        ans[0] = max(A[0][0], A[1][0])
        if len(A[0]) > 1:
            ans[1] = max(ans[0], A[0][1], A[1][1])
        for i in range(2, len(A[0])):
            for j in range(0, 2):
                ans[i] = max(ans[i-2]+A[j][i], ans[i-1], ans[i])
        return ans[-1]


if __name__ == '__main__':
    print(Solution().adjacent([[74, 37, 82, 1],  [66, 38, 16, 1]]))
