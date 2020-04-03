class Solution:
    def lps(self, a):
        i=1
        j=0
        lps_arr = [0]*len(a)
        while i<len(a):
            if a[i]==a[j]:
                lps_arr[i] = j + 1
                i+=1
                j+=1
            else:
                j=lps_arr[j-1]
                if a[i]==a[j]:
                    lps_arr[i] = j + 1
                    i += 1
                    j += 1
                else:
                    while j > 0 and a[j] != a[i]:
                        j = lps_arr[j - 1]
                    if j == 0 and a[i] != a[j]:
                        lps_arr[i] = 0
                        i += 1
                    else:
                        lps_arr[i] = j + 1
                        i += 1
        return lps_arr

    def solve(self, A):
        rev_str = A[::-1]
        concat = A + "$" + rev_str
        lps_ =self.lps(concat)
        return len(A)-lps_[-1]

# print(Solution().solve("hqghumeaylnlfdxfi"))
# print(Solution().solve("banana"))
# print(Solution().solve("abc"))
# print(Solution().solve("aaaaa"))
print(Solution().solve("AACECAAAA"))

# print(Solution().solve("babb"))