class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Return the level (0-indexed) with maximum number of nodes.
from collections import deque


def maxNodeLevel(root):
    # code here
    maxsize = 0
    maxlevel = 0
    que = deque()
    que.append(root)
    que.append('$')
    level_cnt = 0
    level = 0
    while que:
        ele = que.popleft()
        if ele != '$':
            level_cnt += 1
            if ele.left:
                que.append(ele.left)
            if ele.right:
                que.append(ele.right)
        else:
            if maxsize < level_cnt:
                maxlevel = level
                maxsize = level_cnt
            level_cnt = 0
            level += 1
            if len(que) == 0:
                return maxlevel
            que.append('$')
    return maxlevel


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.right.right = Node(3)
    print(maxNodeLevel(root))
