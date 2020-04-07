class Solution:
    def reverse(self, A, i, j):
        while i < j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1
            j -= 1
        return A

    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        breaker = len(nums) - k
        self.reverse(nums, 0, breaker - 1)
        self.reverse(nums, breaker, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    A = [1, 2]
    Solution().rotate(A, 2)
    print(A)
