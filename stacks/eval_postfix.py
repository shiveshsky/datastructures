class Solution:
    def evalRPN(self, A):
        stk = []

        for ele in A:
            if ele not in ["+", "-", "*", "/"]:
                stk.append(ele)
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                if ele == "+":
                    stk.append(a+b)
                elif ele == "-":
                    stk.append(b-a)
                elif ele == "*":
                    stk.append(a*b)
                elif ele == "/":
                    stk.append(b//a)
        return stk.pop()

# print(Solution().evalRPN(["4", "13", "5", "/", "+"])) # 6
print(Solution().evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-" ]))
