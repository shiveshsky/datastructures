class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, A, B=3):
        curr = A
        nxt = curr
        last_last = None
        flag = True
        while nxt is not None:
            prev = None
            last = curr
            ck = B
            while curr is not None and ck > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                ck -= 1

            if flag:
                flag=False
                A = prev
            if last_last is None:
                last_last = last
            else:
                last_last.next = prev
                last_last = last

        return A


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
# a6 = ListNode(6)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
# a5.next = a6
print(Solution().swapPairs(a1))