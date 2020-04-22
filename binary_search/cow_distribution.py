class Solution:
    def feasible_cows(self, A, distance, cows, lenA):
        # we always place first cow at index 0
        c = 1
        # start placing second cow from next distance
        i = 1
        pos = 0
        while i < lenA:
            # only place cow if its position greater that distance
            if A[i] - A[pos] >= distance:
                c += 1
                pos = i
            i += 1
        # check if all cows have been placed
        if c < cows:
            return False
        return True

    def cows(self, A, B):
        # we want to maximize the minimum distance so we do binary search
        # out search space is 1 where first cow will be placed and max(A) where last cow is placed
        # now we take mid distance and try to place cows at mid distance apart in out feasibility function
        # if feasible we record it and search more left as we want to maximize our answer so we go right.
        # the answer space will become like 1 1 1 1 1 0 0 0 so we want to find the last 1.
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
