# Definition for a undirected graph node
from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        queue = deque()
        queue.append(node)
        cloned_grap = None
        address_map = dict()
        while len(queue) > 0:
            ele = queue.popleft()
            if cloned_grap is None:
                cloned_grap = UndirectedGraphNode(ele.label)
                address_map[ele.label] = cloned_grap
                for child in ele.neighbors:
                    if child.label not in address_map:
                        new_child = UndirectedGraphNode(child.label)
                        address_map[child.label] = new_child
                        queue.append(child)
                        cloned_grap.neighbors.append(new_child)
                    else:
                        cloned_grap.neighbors.append(address_map[child.label])
            else:
                for child in ele.neighbors:
                    if child.label not in address_map:
                        new_child = UndirectedGraphNode(child.label)
                        address_map[child.label] = new_child
                        queue.append(child)
                        address_map[ele.label].neighbors.append(new_child)
                    else:
                        address_map[ele.label].neighbors.append(address_map[child.label])

        return cloned_grap


if __name__ == '__main__':
    # root = UndirectedGraphNode(1)
    # root.neighbors.append(UndirectedGraphNode(3))
    # root.neighbors.append(UndirectedGraphNode(2))
    # four = UndirectedGraphNode(4)
    # four.neighbors.append(UndirectedGraphNode(5))
    # four.neighbors.append(UndirectedGraphNode(6))
    # root.neighbors.append(four)

    root = UndirectedGraphNode(703)
    left = UndirectedGraphNode(279)
    right = UndirectedGraphNode(43)

    root.neighbors.append(root)
    root.neighbors.append(left)
    root.neighbors.append(right)

    left.neighbors.append(root)
    left.neighbors.append(left)
    left.neighbors.append(right)

    right.neighbors.append(root)
    right.neighbors.append(left)
    right.neighbors.append(right)

    new_graph = Solution().cloneGraph(root)
    # new_graph = Solution().cloneGraph(root)
    print(new_graph)
