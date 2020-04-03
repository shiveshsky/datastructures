class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def linked_list_length(self, A):
        tmp = A
        cnt = 1
        while tmp is not None:
            cnt += 1
            tmp = tmp.next
        return cnt

    def getIntersectionNode(self, A, B):
        l1 = self.linked_list_length(A)
        l2 = self.linked_list_length(B)
        tmpA = A
        tmpB = B
        if l1<l2:
            incr = l2 - l1
            while incr>0:
                tmpB = tmpB.next
        elif l2<l1:
            incr = l1 - l2
            while incr > 0:
                tmpA = tmpA.next
        while tmpA is not None and tmpB is not None:
            if tmpA == tmpB:
                return tmpA
            tmpB = tmpB.next
            tmpA = tmpA.next
        return None

a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(2)
a5 = ListNode(3)
a6 = ListNode(6)
a7 = ListNode(6)
a8 = ListNode(7)
a9 = ListNode(8)
a10 = ListNode(8)
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

