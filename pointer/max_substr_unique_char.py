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
    print(Solution().lengthOfLongestSubstring("pwwkew"))
