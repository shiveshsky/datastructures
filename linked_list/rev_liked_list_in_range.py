class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, A, B):
        curr = A
        nxt = curr
        ck = B
        prev = None
        while curr is not None and ck > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            ck -= 1
        A.next = nxt
        A = prev


        return A

    def reverseBetween(self, A, B, C):
        tmp = A
        cB = B
        if cB==1:
            A = self.reverse(tmp, C-B+1)
        else:
            while cB > 2:
                tmp = tmp.next
                cB -= 1

            tmp.next = self.reverse(tmp.next, C-B+1)
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
print(Solution().reverseBetween(a1, 2, 4))
