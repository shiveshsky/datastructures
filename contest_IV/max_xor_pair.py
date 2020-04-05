class Solution:
    def get_next_set(self, A, i):
        while i>-1:
            if A[i]=="1":
                break
            i-=1
        return i

    def update(self, A, C):
        copyA = list(A)
        i= self.get_next_set(A, len(A)-1)
        while True:
            copyA[i] = "0"
            if int("".join(copyA), 2)<=C:
                return "".join(copyA)
            copyA[i] = "1"
            i = self.get_next_set(A, i-1)
        return None


    def solve(self, A, B, C):
        binA = bin(A)[2:]
        binC = bin(C)[2:]
        invA = ""
        for i in binA:
            if i=='1':
                invA+="0"
            else:
                invA+="1"
        if len(invA)<len(binC):
            invA = (len(binC)-len(binA))*"1"+invA
        if int(invA,2) >= C:
            invA = self.update(invA, C)
            return A^int(invA, 2)
        else:
            return A^B

print(Solution().solve(3, 5, 6))

