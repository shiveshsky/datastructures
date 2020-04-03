class Solution:
    # @param A : list of integers
    # @return a list of integers
    def shiffter(self, A, n, i, j):
        tmp = A[j]
        while j-1 >=i:
            A[j] = A[j-1]
            j-=1
        A[i] = tmp

    def solve(self, A):
        i=0
        n = len(A)
        while i < n:
            if i % 2 == 0 and A[i] >= 0:
                # probe for a positive and pluck it put shift remaining array to right and place it here if not found break
                j=i
                while j<n and A[j] >= 0:
                    j+=1
                if j==n:
                    break
                self.shiffter(A, n, i, j)
            elif i % 2 != 0 and A[i] < 0:
                # probe for a negative number towards right and pluck it put shift remaining array to right and place it here if not found break
                j = i
                while j < n and A[j] < 0:
                    j += 1
                if j == n:
                    break
                self.shiffter(A, n, i, j)
            i+=1
        return A

    def rightRotate(self, arr, n, outOfPlace, cur):
        temp = arr[cur]
        for i in range(cur, outOfPlace, -1):
            arr[i] = arr[i - 1]
        arr[outOfPlace] = temp
        return arr


    def rearrange(self, arr):
        n = len(arr)
        outOfPlace = -1
        for index in range(n):
            if (outOfPlace >= 0):

                # if element at outOfPlace place in
                # negative and if element at index
                # is positive we can rotate the
                # array to right or if element
                # at outOfPlace place in positive and
                # if element at index is negative we
                # can rotate the array to right
                if ((arr[index] >= 0 and arr[outOfPlace] < 0) or
                        (arr[index] < 0 and arr[outOfPlace] >= 0)):
                    arr = self.rightRotate(arr, n, outOfPlace, index)
                    if (index - outOfPlace > 2):
                        outOfPlace += 2
                    else:
                        outOfPlace = - 1

            if (outOfPlace == -1):

                # conditions for A[index] to
                # be in out of place
                if ((arr[index] >= 0 and index % 2 == 0) or
                        (arr[index] < 0 and index % 2 == 1)):
                    outOfPlace = index
        return arr


# print(Solution().solve([-1, -2, -3, 4, 5, -4, -5, -6]))
print(Solution().solve([ 24, -8, 7, 20, -19, -13, -3, 25, -10, 10, -25, 7, 22, -15, 23, 6, -2, 26, 10, -14, -8, 5, -7, 27, 19, 15, -28, -30, 9, -19, -30, -2, -27, -9, 4, 14, -8, -4, 15, 24, -8, -27, -16, -11, 1, 18, -2, -5, 9, 28, -23, 23, -26, 8, -17, 20, -7, 5, -18, 8, -24, -20, 20, -28, -3, -18, 1, -8, 26, 14, -6, 15, 9, 12, -1, 29, -12, -3, 8, 23, -21, 0, -7, -4, -25, -18, -12, -17, -15, -11, -3, -29, -13, 10, 1, 11, 11, 15, -9, -29, 12, -21, -17, 1, 7, 11, 7, 15, 21, -4, -20, 17, -8, 1, -3, 28, -8, -29, 9, 29, 26, -16, -21, -23, -5, 25, -13, -1, -29, 25, 17, 3, 11, 26, 14, -30, 12, -4, 29, 21, -25, 8, -4, 11, -28, -16, -26 ]))