class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for ch in S:
            if ch !="#":
                stack1.append(ch)
            elif len(stack1)>0:
                stack1.pop()
        for ch in T:
            if ch !="#":
                stack2.append(ch)
            elif len(stack2)>0:
                stack2.pop()
        return stack2==stack1