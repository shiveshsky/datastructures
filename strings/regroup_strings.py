class Solution:
    def solve(self, A):
        A = list(map(int, list(A)))
        return min(self.bring_to_begining(A, 0), self.bring_to_begining(A, 1))

    def bring_to_begining(self, A, dig):
        count = 0
        i=0
        index = 0
        while i<len(A) and index<len(A):
            if A[i] == dig:
                if index<i:
                    count+=(i-index)
                    index+=1
                else:
                    index += 1
            else:
                pass
            i+=1


        return count


print(Solution().solve("1110101"))
