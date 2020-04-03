class Solution:
    def countAndSay(self, A):
        start = 1
        ans = "1"
        for i in range(1, A):
            j = 0
            cnt = 1
            new_ans = ""
            while j < len(ans):
                if j+1<len(ans) and ans[j] == ans[j+1]:
                    cnt+=1
                else:
                    new_ans += str(cnt)+ans[j]
                    cnt=1
                j+=1
            ans = new_ans
        return ans

print(Solution().countAndSay(1))
