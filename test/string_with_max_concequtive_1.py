class Solve:
    def solve(self, A):
        i = 0
        j = 0
        max_len = 0
        zeros = 1
        zero_one = {0: 0, 1: 0}
        while j<len(A) and i<=j:
            if A[j] == 1:
                zero_one[1] += 1
                max_len = max(max_len, (zero_one[0] + zero_one[1]))
                j += 1
            else:
                if zeros > 0:
                    zeros -= 1
                    zero_one[0] += 1
                    max_len = max(max_len, (zero_one[0] + zero_one[1]))
                    j += 1
                else:
                    if i < len(A):
                        if A[i] == 0:
                            zeros += 1
                        zero_one[A[i]] -= 1

                        i += 1
                        max_len = max(max_len, (zero_one[0] + zero_one[1]))

        return max_len


print(Solve().solve([0, 1, 1, 0, 1, 1, 1]))
