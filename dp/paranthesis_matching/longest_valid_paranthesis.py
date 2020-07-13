class Solution:
    def longestValidParentheses(self, A):
        sum = 0
        stack = [-1]

        for i in range(0, len(A)):
            if A[i]=='(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    sum = max(sum, i-stack[-1])
        return sum


if __name__ == '__main__':
    print(Solution().longestValidParentheses("()("))

