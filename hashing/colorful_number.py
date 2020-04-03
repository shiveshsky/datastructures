class Solution:
    def colorful(self, A):
        number = list(str(A))
        pre_prod = self.subsets(number)
        j = -1
        my_set = set()
        k=0
        while k<len(pre_prod):
            i=k
            j=-1
            while i<len(pre_prod):
                if j == -1:
                    if pre_prod[i] not in my_set:
                        my_set.add(pre_prod[i])
                    else:
                        return 0
                    j+=1
                    i+=1
                    continue
                prod = pre_prod[i] // pre_prod[j] if pre_prod[j] !=0 else 0
                if prod in my_set:
                    return 0
                else:
                    my_set.add(prod)
                i+=1
                j+=1
            k+=1
        return 1

    def subsets(self, A):
        pre_prod = []
        pre_prod.append(int(A[0]))
        for i in range(1, len(A)):
            pre_prod.append(int(pre_prod[-1])*int(A[i]))
        return pre_prod


print(Solution().colorful(263))
