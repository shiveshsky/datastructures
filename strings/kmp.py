class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(A) < len(B):
            return -1
        else:
            return self.kmp_str(A, B)


    def kmp_str(self, a, b):
        lps_arr = self.lps(b)
        i = 0
        j = 0
        while i < len(a):
            if a[i] == b[j]:
                i += 1
                j += 1
                if j == len(b):
                    return i - j
            else:
                if j!=0:
                    j=lps_arr[j-1]
                else:
                    i+=1

        return -1

    def lps(self, a):
        lps = [0] * len(a)
        i = 1
        j = 0
        while i < len(a):
            if a[i] == a[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                j = lps[j - 1]
                if a[i] == a[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    while j > 0 and a[j] != a[i]:
                        j = lps[j - 1]
                    if j == 0 and a[i] != a[j]:
                        lps[i] = 0
                        i += 1
                    else:
                        lps[i] = j + 1
                        i += 1
        return lps

print(Solution().lps("banana"))
print(Solution().lps("babb"))
print(Solution().lps("hqghumeaylnlfdxfi"))
print(Solution().lps("abc"))
print(Solution().strStr("bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba", "babaaa"))

