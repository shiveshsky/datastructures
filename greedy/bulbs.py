class Solution:
    def bulbs(self, A):
        count = 0
        for i in range(0, len(A)):
            if A[i]==1 and count%2==0:
                continue
            elif A[i]==0 and count%2==0:
                count+=1
            elif A[i]==0 and count%2!=0:
                continue
            elif A[i]==1 and count%2 != 0:
                count+=1
        return count

if __name__ == '__main__':
    print(Solution().bulbs([0, 1, 0, 1]))
