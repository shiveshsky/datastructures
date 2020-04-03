class Solution:
    def maxArea(self, A):
        i=0
        j=len(A)-1
        max_area = 0
        while i < j:
            area = (j-i)*min(A[i], A[j])
            if A[i] < A[j]:
                i += 1
            elif A[j] < A[i]:
                j -= 1
            elif A[i] == A[j]:
                i += 1
                j -= 1
            max_area = max(max_area, area)
        return max_area
print(Solution().maxArea([1,5,4,3]))

