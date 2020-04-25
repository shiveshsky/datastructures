class Solution:
    def maxProduct(self, A):
        # https://www.youtube.com/watch?v=1s0r7Ixir80
        current_max = A[0]
        current_min = A[0]
        final_max = A[0]
        for i in range(1, len(A)):
            tmp = current_max
            current_max = max(current_max*A[i], current_min*A[i], A[i])
            current_min = min(tmp*A[i], current_min*A[i], A[i])

            final_max = max(final_max, current_max)
        return final_max
