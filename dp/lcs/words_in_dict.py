class Solution:
    # O(n^2)
    def wordBreak(self, s, word_dict):
        stack = [1]
        for i in range(0, len(s)):
            stack.append(0)
            for j in range(i, -1, -1):
                if stack[j] and s[j:i + 1] in word_dict:
                    stack[i + 1] = 1
                    break
        return stack[len(s)]


if __name__ == '__main__':
    print(Solution().wordBreak("myinterviewtrainer", ["interview", "my", "trainer"]))
