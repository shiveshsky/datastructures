class Solution:
    def longestCommonPrefix(self, A):
        prefix= ""
        for i, st in enumerate(A):
            if i == 0:
                prefix+=st
            else:
                sml, lar = (st,prefix) if len(st)<len(prefix) else (prefix, st)
                tmp_pre = ""
                for c in range(len(sml)):
                    if sml[c]!=lar[c]:
                        break
                    else:
                        tmp_pre+=sml[c]
                prefix = tmp_pre if len(tmp_pre)<=len(prefix) else prefix
        return prefix
print(Solution().longestCommonPrefix(["abab", "ab", "abcd"]))
