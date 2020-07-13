class Celebrity:
    def possible_celebrity(self, mat, i, j):
        if mat[i][j] == 1:
            return j
        else:
            return i

    def getId(self, m, n):
        stak = [i for i in range(n)]
        while len(stak) > 1:
            a = stak.pop()
            b = stak.pop()
            stak.append(self.possible_celebrity(m, a, b))
        possible_ans = stak.pop()
        if any(m[possible_ans]):
            return -1
        else:
            return possible_ans
