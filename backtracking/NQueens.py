class Solution:
    rows = {}
    cols = {}
    forward_diag = {}
    backward_diag = {}

    def fill_maps(self, N):
        for i in range(0, N):
            self.rows.update({i: False})
            self.cols.update({i: False})
        for i in range(0, 2*N-1):
            self.forward_diag.update({i: False})
            self.backward_diag.update({i: False})

    def get_backward_diag_key(self, i, j, n):
        for k in range(len(self.backward_diag)):
            if j-i == n-k-1:
                return k

    def get_forward_diag_key(self, i, j, n):
        return i+j

    def isviable(self, i, j, n):

        if self.rows[i]:
            return False
        if self.cols[j]:
            return False
        if self.forward_diag[self.get_forward_diag_key(i, j, n)]:
            return False
        if self.backward_diag[self.get_backward_diag_key(i, j, n)]:
            return False
        return True

    def filler(self, A, queens_so_far, totlaQ, ans, n, Row):
        if queens_so_far==totlaQ:
            temp_ans = []
            for i in range(n):
                r = []
                for j in range(n):
                    r.append(A[i][j])
                temp_ans.append(''.join(r))
            ans.append(temp_ans)
            return
        if queens_so_far > totlaQ:
            return
        if Row>queens_so_far:
            return

        for i in range(Row, len(A)):
            for j in range(0, len(A)):
                if self.isviable(i, j, n):
                    A[i][j]='Q'
                    queens_so_far += 1
                    self.cols[j]=True
                    self.rows[i]=True
                    self.forward_diag[self.get_forward_diag_key(i,j,n)]=True
                    self.backward_diag[self.get_backward_diag_key(i,j,n)]=True
                    self.filler(A, queens_so_far, totlaQ, ans, n, i+1)
                    queens_so_far-=1
                    A[i][j]='.'
                    self.cols[j] = False
                    self.rows[i] = False
                    self.forward_diag[self.get_forward_diag_key(i, j, n)] = False
                    self.backward_diag[self.get_backward_diag_key(i, j, n)] = False
            if i>0 and (not self.rows[i-1]):
                return
        return

    def solveNQueens(self, n):
        self.fill_maps(n)
        ans = []
        A = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            A.append(row)

        self.filler(A, 0, n, ans, n, 0)
        return ans

print(Solution().solveNQueens(10))