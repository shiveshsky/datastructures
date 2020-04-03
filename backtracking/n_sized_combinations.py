class Solve:

    def combi_n_sized(self, n, k, pre, ans):
        if k==0:
            ans.append(pre.copy())
            return
        for i in range(len(n)):
            pre.append(n[i])
            self.combi_n_sized(n[i+1:], k-1, pre, ans)
            pre.pop()
