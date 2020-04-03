class Solution:
    def addBinary(self, A, B):
        if len(A)<len(B):
            A = "0"*(len(B)-len(A)) + A
        elif len(A)>len(B):
            B = "0"*(len(A)-len(B)) + B

        carry = 0
        sum = 0
        ans = ""
        for i in range(len(A)-1, -1, -1):
            if int(A[i])+int(B[i])+carry == 0:
                ans = "0"+ans
            elif int(A[i])+int(B[i])+carry == 1:
                ans = "1"+ans
                if carry == 1:
                    carry = 0
            elif int(A[i])+int(B[i])+carry == 2:
                ans = "0"+ans
                carry = 1
            elif int(A[i])+int(B[i])+carry == 3:
                ans = "1"+ans
                carry = 1
        if carry == 1:
            ans = "1"+ans
        return ans
print(Solution().addBinary("0", "0"))
