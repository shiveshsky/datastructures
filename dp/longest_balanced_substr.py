class Solution:
    def LBSlength(self, A):
        stack = []
        stack.append(0)
        ans = 0
        for i in range(1, len(A)):
            if len(stack) == 0:
                stack.append(i)
                continue
            elif A[i] == '>':
                if A[stack[-1]] == '<':
                    stack.pop()
                    if len(stack)>0:
                        ans = max(ans, i-stack[-1])
                    else:
                        ans = i+1
                else:
                    stack.append(i)
            elif A[i] == '}':
                if A[stack[-1]] == '{':
                    stack.pop()
                    if len(stack)>0:
                        ans = max(ans, i-stack[-1])
                    else:
                        ans = i+1
                else:
                    stack.append(i)
            elif A[i] == ')':
                if A[stack[-1]] == '(':
                    stack.pop()
                    if len(stack)>0:
                        ans = max(ans, i-stack[-1])
                    else:
                        ans = i+1
                else:
                    stack.append(i)
            elif A[i] == ']':
                if A[stack[-1]] == '[':
                    stack.pop()
                    if len(stack)>0:
                        ans = max(ans, i-stack[-1])
                    else:
                        ans = i+1
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().LBSlength("<<<<>"))