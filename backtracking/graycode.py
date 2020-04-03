class Solution:

    def grayCode(self, A):
        if A==1:
            return [0, 1]
        neucleus = ['00', '01', '11', '10']
        if A==2:
            ans = []
            for nu in neucleus:
                ans.append(int(nu, 2))

        for i in range(3, A+1):
            neucleus += neucleus[::-1]
            half = (2**i)//2
            # fill zero
            for j in range(0, half):
                neucleus[j]='0'+neucleus[j]
            for k in range(half, 2**i):
                neucleus[k]='1'+neucleus[k]

        ans = []
        for nu in neucleus:
            ans.append(int(nu, 2))
        return ans
print(Solution().grayCode(2))
