class Solution:
    def solve(self, A, B):
        la = list(A)
        cnt = 0
        for i in range(0, len(la)):
            if la[i] == '0' and (i+B) <= len(la):
                cnt += 1
                for j in range(i, i+B):
                    if j<len(la):
                        la[j] = '0' if la[j]=='1' else '1'
                    else:
                        break
        try:
            la.index('0')
            return -1
        except ValueError:
            return cnt


if __name__ == '__main__':
    print(Solution().solve("011", 3))
