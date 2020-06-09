class Node:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if root is None:
        return None
    if root.val == n1 or root.val == n2:
        return root
    leftLCA = findLCA(root.left, n1, n2)
    rightLCA = findLCA(root.right, n1, n2)
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA is not None else rightLCA


count = 0


def countTurn(root, val, turn):
    global count
    if root is None:
        return False
    if root.val == val:
        return True
    if turn:
        if countTurn(root.left, val, turn):
            return True
        if countTurn(root.right, val, not turn):
            count += 1
            return True
    else:
        if countTurn(root.right, val, turn):
            return True
        if countTurn(root.left, val, not turn):
            count += 1
            return True
    return False


# Function to find nodes common to given two nodes
def numberOfTurn(root: Node, first: int, second: int) -> int:
    global count
    LCA = findLCA(root, first, second)

    # there is no path between these two node
    if LCA is None:
        return -1

    count = 0

    # case 1:
    if LCA.key != first and LCA.key != second:

        # count number of turns needs to reached
        # the second node from LCA
        if countTurn(LCA.right, second, False) or countTurn(
                LCA.left, second, True):
            pass

        # count number of turns needs to reached
        # the first node from LCA
        if countTurn(LCA.left, first, True) or countTurn(
                LCA.right, first, False):
            pass
        return count + 1

    # case 2:
    if LCA.key == first:

        # count number of turns needs to reached
        # the second node from LCA
        countTurn(LCA.right, second, False)
        countTurn(LCA.left, second, True)
        return count
    else:

        # count number of turns needs to reached
        # the first node from LCA1
        countTurn(LCA.right, first, False)
        countTurn(LCA.left, first, True)
        return count
