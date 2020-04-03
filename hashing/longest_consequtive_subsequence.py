class Solution:
    def longestConsecutive(self, A):

        my_set = set(A)
        len_current = 0
        max_len = 0
        for i in A:
            if i-1 not in my_set:
                # possible left boundary
                start = i
                len_current = 0
                while start in my_set:
                    len_current+=1
                    start+=1
                max_len = max(max_len, len_current)
        return max_len
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

