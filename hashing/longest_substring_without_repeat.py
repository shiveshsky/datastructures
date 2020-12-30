# class Solution:
#     def lengthOfLongestSubstring(self, A):
#         my_map = {}
#         i=0
#         max_len = 0
#         while i < len(A):
#             if my_map.get(A[i]) is not None:
#                 i=my_map.get(A[i])+1
#                 max_len = max(max_len, len(my_map))
#                 my_map = {}
#                 continue
#             else:
#                 my_map[A[i]] = i
#             i+=1
#         max_len = max(max_len, len(my_map))
#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        j = 0
        ms = set()
        while j < len(s):
            if s[j] not in ms:
                ms.add(s[j])
                ans = max(ans, (j - i) + 1)
                j += 1

            else:
                while s[i] != s[j]:
                    ms.remove(s[i])
                    i += 1
                i += 1
                j += 1
        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
