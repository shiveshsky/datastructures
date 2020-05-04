from collections import Counter


class Solution:
    def isPalindrome(self, A):
        h = len(A)-1
        l = 0
        while h > l:
            if A[l] == A[h]:
                l += 1
                h -= 1
            else:
                return False
        return True

    def anytwo(self, A):
        freq = Counter(A)
        k=0
        for key, v in freq.items():
            if v > 2:
                return True
        A = list(A)
        for i in range(0, len(A)):
            if freq[A[i]]>1:
                A[k]=A[i]
                k+=1
        # A[k] = '\0'
        if self.isPalindrome(A[0:k]):
            if k%2 !=0:
                return A[k//2] == A[k//2-1]
            return False
        return True


if __name__ == '__main__':
    print(Solution().anytwo('abba'))