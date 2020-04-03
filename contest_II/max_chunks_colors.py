class Solution:
    def solve(self, A):
        c = 0
        # max_so_far = -1
        # A.insert(0,0)
        visited = set()
        for i in range(0, len(A)):
            if A[i]==i+1 and A[i] not in visited:
                c+=1
            else:
                j = i
                if A[j] not in visited:
                    while A[j] != i+1:
                        tmp = A[j]
                        visited.add(tmp)
                        visited.add(A[tmp-1])
                        A[j] = A[tmp-1]
                        A[tmp-1] = tmp
                    c+=1
        return c

print(Solution().solve([5,2,3,4,1,7,6]))
# print(Solution().solve([7,12,9,18,5,13,6,14,17,2,1,15,10,11,4,3,8,16]))
                        # 1  2  3 4 5  6 7  8 9  1

#  5 2 3 4 1 7 6 ==>5

# 0 2 3 4 0 7 6