class Solution:
    def lengthOfLongestSubstring(self, A):
        my_map = {}
        i=0
        max_len = 0
        while i < len(A):
            if my_map.get(A[i]) is not None:
                i=my_map.get(A[i])+1
                max_len = max(max_len, len(my_map))
                my_map = {}
                continue
            else:
                my_map[A[i]] = i
            i+=1
        max_len = max(max_len, len(my_map))
        return max_len
print(Solution().lengthOfLongestSubstring("bbbb"))



