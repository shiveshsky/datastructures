class Solution:
    def feasible_cows(self, A, distance, cows, lenA):
        c = 1
        i = 1
        pos = 0
        while i < lenA:
            if A[i] - A[pos] >= distance:
                c += 1
                pos = i
            i += 1
        if c < cows:
            return False
        return True

    def cows(self, A, B):
        answer_space_l = 1
        answer_space_h = sum(A)
        ans = -1
        lenA = len(A)
        while answer_space_l < answer_space_h:
            answer_space_m = (answer_space_l + answer_space_h) // 2
            if self.feasible_cows(A, answer_space_m, B, lenA):
                ans = max(ans, answer_space_m)
                answer_space_l = answer_space_m + 1
            else:
                answer_space_h = answer_space_m - 1
        return ans
