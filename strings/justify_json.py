class Solution:
    def prettyJSON(self, A):
        tab = 0
        ans = []
        tmp_str = ""
        for i, chr in enumerate(A):
            if chr == '{' or chr == '[':
                ans.append(tmp_str)
                tmp_str = "\t"*tab+chr
                tab += 1
                ans.append(tmp_str)
                tmp_str = ""
            elif chr == '}' or chr == ']':
                ans.append(tmp_str)
                tab -= 1

                tmp_str = "\t"*tab + chr
                ans.append(tmp_str)
                tmp_str = ""
            elif chr == ',':
                if A[i-1] == '}' or A[i-1]==']':
                    ans[-1]+=chr
                else:
                    ans.append(tmp_str+chr)
                    tmp_str = ""
            else:
                if tmp_str == "":
                    tmp_str += "\t"*tab+chr
                else:
                    tmp_str += chr
        new_ans = []
        for wor in ans:
            if len(wor)>0:
                new_ans.append(wor)

        return new_ans


# print(Solution().prettyJSON('{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'))
for i in Solution().prettyJSON('{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'):
    print(i)
