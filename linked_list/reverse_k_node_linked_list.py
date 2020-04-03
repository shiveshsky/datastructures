class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, A, B):
        if A is None:
            return
        curr = A
        prev = None
        nxt = None
        ck = B
        while curr is not None and ck > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            ck -= 1
        if nxt is not None:
            A.next = self.reverseList(nxt, B)
        return prev


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
print(Solution().reverseList(a1, 2))