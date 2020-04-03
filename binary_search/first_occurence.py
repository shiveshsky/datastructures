class Solve:

    def bianryFirstOccs(self, A, i):
        l = 0
        h = len(A)-1
        while l <= h:
            mid = (l+h)//2
            if A[mid]<i:
                l=mid+1
            elif A[mid]>i:
                h=mid-1
            else:
                if mid-1>=0 and A[mid-1]==A[mid]:
                    h=mid-1
                else:
                    return mid
        return -1
