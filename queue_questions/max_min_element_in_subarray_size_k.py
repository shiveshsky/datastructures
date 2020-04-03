class Solution:
    def max_element_in_window(self, A, B):
        start = 0
        dek = []
        ans = []
        i = 0
        while i < len(A):
            if len(dek) == 0:
                dek.append(i)
            else:
                if A[i] <= A[dek[-1]]:
                    dek.append(i)
                else:
                    while len(dek) > 0 and A[dek[-1]] < A[i]:
                        dek.pop()
                    dek.append(i)
            if i - start == B-1:
                ans.append(dek[0])
                start += 1
                if start>dek[0]:
                    dek.pop(0)
            i += 1

        return ans

    def min_element_in_window(self, A, B):
        start = 0
        dek = []
        ans = []
        i = 0
        while i < len(A):
            if len(dek) == 0:
                dek.append(i)
            else:
                if A[i] > A[dek[-1]]:
                    dek.append(i)
                else:
                    while len(dek) > 0 and A[dek[-1]] > A[i]:
                        dek.pop()
                    dek.append(i)
            if i - start == B - 1:
                ans.append(dek[0])
                start += 1
                if start > dek[0]:
                    dek.pop(0)
            i += 1

        return ans

    def solve(self, A, B):
        mod = 1000000007
        max_elements = self.max_element_in_window(A, B)
        min_elements = self.min_element_in_window(A, B)
        sum = 0
        for i in range(0, len(max_elements)):
            sum=((A[max_elements[i]]%mod+A[min_elements[i]]%mod)%mod + sum%mod)
        return sum%mod

print(Solution().solve([2, 5, -1, 7, -3, -1, -2], 4))
