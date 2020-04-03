import math
from bisect import bisect_right, bisect_left


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def bsearch(self, prefixsum, n, k):

        # Initialize result
        # Do Binary Search for largest
        # subarray size
        ans, left, right = -1, 1, n

        while (left <= right):

            mid = (left + right) // 2

            for i in range(mid, n + 1):

                if (prefixsum[i] - prefixsum[i - mid] > k):
                    i = i - 1
                    break
            i = i + 1
            if (i == n + 1):
                left = mid + 1
                ans = mid
                # We found a subrray of size mid with sum
            # greater than k
            else:
                right = mid - 1

        return ans


    def solve(self, A, B):
        prefixsum = [0 for x in range(len(A) + 1)]

        # Finding prefix sum of the array.
        for i in range(len(A)):
            prefixsum[i + 1] = prefixsum[i] + A[i]

        return self.bsearch(prefixsum, len(A), B);

    def findMedian(self, A):
        search_space_l = A[0][0]
        search_space_h = 0
        for row in A:
            search_space_h=max(row[-1], search_space_h)
        expected_freq = (len(A)*len(A[0])+1)//2
        while search_space_l < search_space_h:
            search_space_m = (search_space_l+search_space_h)//2
            has_freq = 0
            for row in A:
                has_freq += bisect_right(row, search_space_m)
            if has_freq < expected_freq:
                search_space_l = search_space_m+1
            else:
                search_space_h = search_space_m
        return search_space_l


    def solve_pwww(self, A):
        current_sum=0
        arr_ans = []
        while A!=0:
            arr_ans.append(A%3)
            A=A//3
        final_ans=[]
        power = 0
        for rem in arr_ans:
            if rem==0:
                pass
            if rem==1:
                final_ans.append(rem*(3**power))
            if rem==2:
                pwr = 3**power
                final_ans.append(pwr)
                final_ans.append(pwr)
            power+=1
        return final_ans

    def countKdivPairs(self, A, n, K):

        # Create a frequency array to count
        # occurrences of all remainders when
        # divided by K
        freq = [0] * K

        # Count occurrences of all remainders
        for i in range(n):
            freq[A[i] % K] += 1

        # If both pairs are divisible by 'K'
        sum = freq[0] * (freq[0] - 1) / 2;

        # count for all i and (k-i)
        # freq pairs
        i = 1
        while (i <= K // 2 and i != (K - i)):
            sum += freq[i] * freq[K - i]
            i += 1

        # If K is even
        if (K % 2 == 0):
            sum += (freq[K // 2] * (freq[K // 2] - 1) / 2);

        return int(sum)

    def make_set(self, A, prefix, ans):
        if len(A) == 1:
            ans.append(prefix+A)
            return
        for i in range(0, len(A)):
            prefix.append(A[i])
            ans.append(prefix.copy())
            for j in range(i+1, len(A)):
                self.make_set(A[j:], prefix, ans)
                break
            prefix.pop()

    def isfiesible(self, A, B):
        count = 0
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                val = B - (A[i] + A[j])
                if val < 0:
                    break
                else:
                    ind = bisect_left(A, val)
                    if ind>j:
                        count += 1
        if count <= B:
            return True
        else:
            return False

    def solve_b(self, A, B):
        A.sort()
        l = A[0]
        h = A[-1] + A[-2] + A[-3]
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            if self.isfiesible(A, mid):
                ans = max(l, ans)

                l = mid+1
            else:
                h = mid - 1
        print(mid, l, h, ans)




# print(Solution().sixlets([5,17,1000, 11], 4))
# print(ans)
# print(Solution().unique_paths([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
# print(Solution().newKthpermut([1,2,3,4,5,6,7,8,9,10,11], 1, [], ans))
# Solution().find_new_str('1234', 7)
# Solution().combi_n_sized([1,2,3,4], 2, [], ans)

# print(''.join(map(str, ans)))

# ll = [ 8, 10, 6, 11, 1, 16, 8 ] # [1, 6 , 8, 8, 10, 11, 16]
# ll.sort()
# ll = [10, 1, 2, 7, 6, 1, 5]
# ll.sort()
# ans = []
# Solution().combo_sum(ll, 8, [], ans)
# print(ans)

# print(Solution().countKdivPairs([2,2,1,7,5,3],6,4))
# print(Solution().solve_pwww(411))
# print(Solution().pivot([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100]))
# print(Solution().goodbasesolve(6409967103))
# print(Solution().paint([1,11], 1, 2))
# print(Solution().sqrt(393))
# print(Solution().cows([82, 61, 38, 88, 12, 7, 6, 12, 48, 8, 31, 90, 35, 5, 88, 2, 66, 19, 5, 96, 84, 95], 8))
# print(Solution().books([ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ], 26)) # 97
# print(Solution().book_feasibility([ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ],97, 26))
# print(Solution().books([73, 58, 30, 72, 44, 78, 23, 9], 5)) # 110
# print(Solution().bianryFirstOccs([2,2,2,2,2,2,3,3,3,3],2))
# print(Solution().findMedian([[1, 3, 5],
#             [2, 6, 9],
#             [3, 6, 9]]))
# print(Solution().solve( [ 2, 24, 38, 25, 35, 33, 43, 12, 49, 35, 45, 47, 5, 33], 1249)) # 6
# print(Solution().solve([1,2,3,4,5], 10))
# print(Solution().solve([5,17,100,11], 130))