class Solve:
    def all_permut(self, A, prefix, ans):
        unique_digits = set(A)
        if len(unique_digits) == 1:
            ans.append(prefix+A)
            return
        if len(A)==0:
            ans.append()
            return
        i=0
        while i < len(A):
            prefix.append(A[i])
            self.all_permut(A[0:i]+A[i+1:], prefix, ans)
            while i+1<len(A) and A[i]==A[i+1]:
                i+=1
            prefix.pop(-1)
            i+=1
