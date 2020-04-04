class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        prev = root
        current = root.left
        while current is not None:
            flag = True
            current_start = current
            while prev is not None:
                if flag:
                    current.next = prev.right
                    prev = prev.next
                    current = current.next
                    flag=False
                else:
                    current.next = prev.left
                    current = current.next
                    flag = True

            prev = current_start
            current = current_start.left
        return root

root = TreeLinkNode(1)
l1 = TreeLinkNode(2)
r1 = TreeLinkNode(5)
root.left=l1
root.right=r1
l1.left=TreeLinkNode(3)
l1.right=TreeLinkNode(4)
r1.left=TreeLinkNode(6)
r1.right=TreeLinkNode(7)
Solution().connect(root)

