class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect_loop(self, root):
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
                    flag = False
                else:
                    current.next = prev.left
                    current = current.next
                    flag = True

            prev = current_start
            current = current_start.left
        return root

    def connect(self, root):
        if root is None:
            return None
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root


if __name__ == '__main__':
    root = TreeLinkNode(-1)
    root.left = TreeLinkNode(0)
    root.right = TreeLinkNode(1)
    root.left.left = TreeLinkNode(2)
    root.left.right = TreeLinkNode(3)
    root.right.left = TreeLinkNode(4)
    root.right.right = TreeLinkNode(5)
    root.left.left.left = TreeLinkNode(6)
    root.left.left.right = TreeLinkNode(7)
    root.left.right.left = TreeLinkNode(8)
    root.left.right.right = TreeLinkNode(9)
    root.right.left.left = TreeLinkNode(10)
    root.right.left.right = TreeLinkNode(11)
    root.right.right.left = TreeLinkNode(12)
    root.right.right.right = TreeLinkNode(13)
    Solution().connect(root)

# root = TreeLinkNode(1)
# l1 = TreeLinkNode(2)
# r1 = TreeLinkNode(5)
# root.left=l1
# root.right=r1
# l1.left=TreeLinkNode(3)
# l1.right=TreeLinkNode(4)
# r1.left=TreeLinkNode(6)
# r1.right=TreeLinkNode(7)
# Solution().connect(root)
