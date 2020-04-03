class Solve:
    def combo_sum(self, A, k, prev, ans):
        if k == 0:
            ans.append(prev.copy())
            return

        if k < 0:
            return

        if len(A) == 1:
            if A[0] == k:
                ans.append(prev+A)
            return
        i=0
        while i< len(A):
            prev.append(A[i])
            self.combo_sum(A[i+1:], k-A[i], prev, ans)
            while i+1<len(A) and A[i]==A[i+1]:
                i+=1
            prev.pop()
            i += 1
