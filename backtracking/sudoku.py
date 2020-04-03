class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    dict_rows = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set()
    }
    dict_cols = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set()
    }
    dict_square = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set()
    }

    def solveSudoku(self, A):
        sud_mat = []
        self.dict_rows = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        self.dict_cols = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        self.dict_square = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }

        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                if A[i][j]!='.':
                    int_val = int(A[i][j])
                    row.append(int_val)
                    self.dict_rows[i].add(int_val)
                    self.dict_cols[j].add(int_val)
                    self.dict_square[self.get_square([i,j])].add(int_val)
                else:
                    row.append((0))
            sud_mat.append(row)
        ans = []
        self.fill_vals(sud_mat, ans)
        # final_ans = []
        # for row in ans:
        #     final_ans.append(''.join(map(str, row)))
        # return ' '.join(final_ans)
        # for i in range(0, len(A)):
        #     for j in range(0, 9):
        #         ll = list(A[i])
        #         ll[j]=str(ans[i][j])
        #         A[i]="".join(ll)
        # return A
        A.clear()
        for i in range(len(ans)):
            A.append([str(j) for j in  ans[i]])
        return A

    def check_solved(self, A):
        for k,v in self.dict_square.items():
            if len(v)<9:
                return False
        for k,v in self.dict_rows.items():
            if len(v)<9:
                return False
        for k,v in self.dict_cols.items():
            if len(v)<9:
                return False
        return True

    def fill_vals(self, A, ans):
        if self.check_solved(A):
            for i in range(9):
                r = []
                for j in range(9):
                    r.append(A[i][j])
                ans.append(r)
            return
        for i in range(0, 9):
            for j in range(0, 9):
                viable_flag_if_zero = False
                for val in range(1, 10):
                    if A[i][j] == 0:
                        if self.check_viability([i, j], val):
                            viable_flag = True
                            A[i][j] = val
                            square = self.get_square([i, j])
                            self.dict_cols[j].add(val)
                            self.dict_rows[i].add(val)
                            self.dict_square[square].add(val)
                            self.fill_vals(A, ans)
                            A[i][j] = 0
                            self.dict_cols[j].discard(val)
                            self.dict_rows[i].discard(val)
                            self.dict_square[square].discard(val)
                        else:
                            pass
                    else:
                        viable_flag_if_zero=True
                        break
                if not viable_flag_if_zero:
                    return

    def check_viability(self, location, number):
        if number in self.dict_rows[location[0]]:
            return False
        if number in self.dict_cols[location[1]]:
            return False
        if number in self.dict_square[self.get_square(location)]:
            return False
        return True

    def get_square(self, location):
        x = location[0]
        y = location[1]

        if 0 <= x <= 2:
            if 0 <= y <= 2:
                return 0
            elif 3 <= y <= 5:
                return 1
            elif 6 <= y <= 8:
                return 2
        elif 3 <= x <= 5:
            if 0 <= y <= 2:
                return 3
            elif 3 <= y <= 5:
                return 4
            elif 6 <= y <= 8:
                return 5
        elif 6 <= x <= 8:
            if 0 <= y <= 2:
                return 6
            elif 3 <= y <= 5:
                return 7
            elif 6 <= y <= 8:
                return 8


# print(Solution().solveSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]))
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]
B =  [ "..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.." ]
Solution().solveSudoku(A)
Solution().solveSudoku(B)
print(A)
print(B)