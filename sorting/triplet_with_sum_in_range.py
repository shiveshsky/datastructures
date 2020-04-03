class Solution:
    def solve(self, A):
        A = list(map(float, A))
        window = []
        window.append(A[0])
        window.append(A[1])
        window.append(A[2])
        window.sort()
        sum_of_window = sum(window)
        for i in range(3, len(A)):
            if sum_of_window > 1.0:
                window[2] = A[i]
                sum_of_window = sum(window)
            elif sum_of_window < 1.0:
                window[0] = A[i]
                sum_of_window = sum(window)

            if 1 < sum_of_window < 2:
                return 1
            window.sort()

        return 0

print(Solution().solve(["0.297657", "0.420048", "0.053365", "0.437979", "0.375614", "0.264731", "0.060393", "0.197118", "0.203301", "0.128168" ]))


