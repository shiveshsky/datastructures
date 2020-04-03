class Solution:
    def solve(self, A, B):
        i=0
        j=-1
        sum=0
        while j < len(A):
            if  sum<B:
                j+=1
                if j<len(A):
                    sum+=A[j]
            elif sum>B:
                if i<len(A):
                    sum-=A[i]
                i+=1
            elif sum==B:
                return [i, j]


        return [-1]
print(Solution().solve([1,2,3,4,5], 5))
# print(Solution().solve([5, 10, 20, 100, 105], 110))
