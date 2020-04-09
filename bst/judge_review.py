class TreeNode:
    def __init__(self, x, i):
       self.val = x
       self.index = i
       self.left = None
       self.right = None
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def __init__(self):
        self.root = None

    def solve(self, A, B):
        good_words = set(A.split("_"))
        for index, line in enumerate(B):
            review = line.split("_")
            count = 0
            for rev in review:
                if rev in good_words:
                    count += 1
            if self.root is None:
                self.root = self.create_bst(self.root, count, index)
            else:
                self.create_bst(self.root, count, index)
        return self.inorderTraversal()[::-1]

    def inorderTraversal(self):
        stack = []
        ans = []
        current = self.root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                ans.append(current.index)
                current = current.right
            else:
                break
        return ans


    def create_bst(self,node, val, index):
        if node is None:
            return TreeNode(val, index)
        elif node.val < val:
            node.right = self.create_bst(node.right, val, index)
        elif node.val >= val:
            node.left = self.create_bst(node.left, val, index)
        return node

if __name__ == '__main__':
    print(Solution().solve("cool_ice_wifi", [ "water_is_cool", "cold_ice_drink", "cool_wifi_speed" ]))