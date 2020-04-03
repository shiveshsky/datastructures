class Solution:
    def isTimeFiseble(self, A, time, painters):
        p = 1
        i = 0
        t = 0
        while i < len(A):
            t += A[i]
            if t > time:
                p += 1
                if p > painters:
                    return False
                t = A[i]
            i += 1
        return True

    def paint(self, A, B, C):
        answer_space_l = max(A)
        answer_space_h = sum(A)
        ans = 99999999
        while answer_space_l <= answer_space_h:
            mid = (answer_space_l + answer_space_h) // 2
            if self.isTimeFiseble(A, mid, C):
                answer_space_h = mid - 1
                ans = min(ans, mid)
            else:
                answer_space_l = mid + 1
        return (ans % 10000003 * B % 10000003) % 10000003


print(Solution().paint([1, 8, 11, 3], 1, 2))
