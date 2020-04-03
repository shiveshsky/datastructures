class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stk = []
        for char in A:
            if char in "(*+-/":
                stk.append(char)
            elif char==")":
                if stk.pop()=="(":
                    return 1
                stk.pop()

        return 0


# print(Solution().braces("(a+(a+b))"))

print(Solution().braces("((a-b+c)*b)"))