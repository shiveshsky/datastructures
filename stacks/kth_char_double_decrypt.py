

class Solution:
    def solve(self, A, B):
        length = 0
        stk = []
        freq = ''
        for char in A:
            if str.isalpha(char):
                fre = int(freq) if freq else 1
                length=(length*int(fre))+1
                if length>B:
                    break
                stk.append((char, length))
                freq = ''

            else:
                freq += char
        while len(stk)>0:
            c,l = stk.pop()
            if B%l==0:
                return c
            else:
                B = B%l
print(Solution().solve("x2y3", 3))
