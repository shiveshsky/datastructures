class Solution:
    def subsets(self, A):
        A.sort()
        ans = [[]]
        self.make_set(A, [], ans)
        return ans

    def make_set(self, A, prefix, ans):
        if len(A) == 1:
            ans.append(prefix + A)
            return
        for i in range(0, len(A)):
            prefix.append((A[i]))
            ans.append(prefix.copy())
            if i + 1 < len(A):
                self.make_set(A[i + 1:], prefix, ans)
            prefix.pop()


# print(Solution().subsets([1, 2, 3]))  # 1, 2, 3, (1,2), (1,3), (1,2,3), (2,3), ()
print(Solution().subsets([1, 2, 3, 4]))