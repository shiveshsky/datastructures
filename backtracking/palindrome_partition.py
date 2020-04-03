class Solution:
    def palindrome_partition(self, A, prev, ans):
        if len(A)==1:
            prev.append(A)
            ans.append(prev.copy())
            prev.pop()
            return
        if len(A)==0:
            ans.append(prev.copy())
            return
        for i in range(1, len(A)+1):
            if self.is_palindrome(A[0:i]):
                prev.append(A[0:i])
                self.palindrome_partition(A[i:], prev, ans)
                prev.pop()
ans = []
Solution().palindrome_partition('nitin', [], ans)