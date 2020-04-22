class Solution:
    def solve(self, A):
        count =1
        i=2
        while i<=A//2:
            if A%i==0:
                count+=1
            i+=1
        return count


if __name__ == '__main__':
    print(Solution().solve(4))
