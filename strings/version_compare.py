class Solution:
    def compareVersion(self, A, B):
        a = A.split(".")
        b = B.split(".")
        if len(a)<len(b):
            while len(a) < len(b):
                a.append("0")
        elif len(b)<len(a):
            while len(b) < len(a):
                b.append("0")
        i=0
        while i<len(a):
            if int(a[i])>int(b[i]):
                return 1
            elif int(a[i])<int(b[i]):
                return -1
            else:
                i+=1
        return 0


print(Solution().compareVersion("1.13", "1.13.1"))


