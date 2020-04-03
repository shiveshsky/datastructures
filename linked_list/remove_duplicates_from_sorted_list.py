class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, A):
        tmp = A
        while tmp is not None:
            if tmp.next is not None and tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return A

    def deleteDuplicatesII(self, A):
        tmp = A
        prev = None
        flag = False
        while tmp is not None:
            while tmp.next is not None and tmp.val == tmp.next.val:
                flag = True
                tmp = tmp.next
            if flag:
                tmp = tmp.next
                flag = False
            if tmp == A:
                prev = tmp
                tmp = tmp.next
            else:
                if prev is None:
                    if tmp is not None and tmp.next is not None and tmp.next.val == tmp.val:
                        continue
                    A = tmp
                    prev = tmp
                    if tmp is not None:
                        tmp = tmp.next
                else:
                    if tmp is not None and tmp.next is not None and tmp.next.val == tmp.val:
                        continue
                    prev.next = tmp
                    prev = tmp
                    if tmp is not None:
                        tmp = tmp.next
                    # if tmp.next is not None:
                    #     tmp = tmp.next.next
                    # else:
                    #     tmp = tmp.next
        return A



a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(2)
a5 = ListNode(3)
a6 = ListNode(6)
# a7 = ListNode(6)
# a8 = ListNode(7)
# a9 = ListNode(8)
# a10 = ListNode(8)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
# a6.next = a7
# a7.next = a8
# a8.next = a9
# a9.next = a10
print(Solution().deleteDuplicatesII(a1))
