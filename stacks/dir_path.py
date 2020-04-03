import re


class Solution:
    def simplifyPath(self, A):
        A = A.strip('/')
        path = re.split(r"/+", A)
        stk = []
        for ele in path:
            if ele not in ['.', '..']:
                stk.append(ele)
            elif ele == '..':
                if len(stk) > 0:
                    stk.pop()
        resolved_path = '/'.join(stk)
        return '/'+resolved_path


# print(Solution().simplifyPath('/Users/shivesh/./anlyz/./sporact/../sporact_mistral'))
print(Solution().simplifyPath('/home//foo/'))
