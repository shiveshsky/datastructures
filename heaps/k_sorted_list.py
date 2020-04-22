# Definition for singly-linked list.
from heapq import heappop, heappush, heapify


class CustomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val<other.val


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        ans_linked_list = None
        next = None
        minheap = []
        heapify(minheap)
        for nodes in A:
            custom_node = CustomListNode(nodes.val)
            custom_node.next = nodes.next
            heappush(minheap, custom_node)
        while len(minheap) > 0:
            min_val = heappop(minheap)
            if ans_linked_list is None:
                ans_linked_list = ListNode(min_val.val)
                next = ans_linked_list
            else:
                next.next = ListNode(min_val.val)
                next = next.next
            if min_val.next is not None:
                next_node = CustomListNode(min_val.next.val)
                next_node.next = min_val.next.next
                heappush(minheap, next_node)
        return ans_linked_list


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(10)
    l1.next.next = ListNode(20)

    l2 = ListNode(4)
    l2.next = ListNode(11)
    l2.next.next = ListNode(13)

    l3 = ListNode(3)
    l3.next = ListNode(8)
    l3.next.next = ListNode(9)

    head = Solution().mergeKLists([l1, l2, l3])
    print(head)