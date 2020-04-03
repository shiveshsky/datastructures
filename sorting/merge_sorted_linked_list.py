class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        i = A
        j = B
        new = None
        ptr = new
        while i and j:
            if i.val < j.val:
                tmp = ListNode(i.val)
                tmp.next = None

                if new is None:
                    new = tmp
                    ptr = tmp
                else:
                    ptr.next = tmp
                    ptr = ptr.next
                i=i.next
            else:
                tmp = ListNode(j.val)
                tmp.next = None

                if new is None:
                    new = tmp
                    ptr = tmp
                else:
                    ptr.next = tmp
                    ptr = ptr.next
                j = j.next
        if i is not None:
            ptr.next = i
        elif j is not None:
            ptr.next = j
        return new


a1 = ListNode(5)
a1.val = 5
# a2 = ListNode(8)
# a2.val = 8
# a3 = ListNode(20)
# a3.val = 20
head1 = a1
# a1.next = a2
# a2.next = a3

b1 = ListNode(4)
b1.val = 4
b2 = ListNode(11)
b2.val = 11
b3 = ListNode(15)
b3.val = 15
head2 = b1
b1.next = b2
b2.next = b3

Solution().mergeTwoLists(head1, head2)
