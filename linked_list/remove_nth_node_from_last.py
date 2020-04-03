# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, A, B):
        pointer1 = A
        pointer2 = A
        jump = B
        while pointer2.next is not None and jump > 0:
            pointer2 = pointer2.next
            jump -= 1
        if jump > 0:
            return A.next
        while pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if pointer1.next is not None:
            pointer1.next = pointer1.next.next

        return A


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
print(Solution().removeNthFromEnd(a1, 1))