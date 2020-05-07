class Solution:
    def isInterleave(self, A, B, C):
        return 1 if self.isInterleaving(A, B, C) else 0

    def isInterleaving(self, A, B, C):
        if len(C) == 0:
            if len(A) == 0 and len(B) == 0:
                return True
            else:
                return False
        if len(A) == 0 and C == B:
            return True
        if len(B) == 0 and A == C:
            return True
        r1 = False
        r2 = False
        if len(A)>=1 and C[0] == A[0]:
            r1 = self.isInterleaving(A[1:], B, C[1:])
        if len(B)>=1 and C[0] == B[0]:
            r2 =  self.isInterleaving(A, B[1:], C[1:])
        return r1 or r2


if __name__ == '__main__':
    print(Solution().isInterleave("eZCHXr0CgsB4O3TCDlitYI7kH38rEElI", "UhSQsB6CWAHE6zzphz5BIAHqSWIY24D", "eUZCHhXr0SQsCgsB4O3B6TCWCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D"))

