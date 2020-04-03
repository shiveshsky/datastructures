# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # wrong you are using extra space
    # reverse the linked list after n//2
    # and compare 0 with mid+1 and so on to achieve solution in O(n)
    def lPalin(self, A):
        tmp_head = A
        stk = []
        while tmp_head != None:
            stk.append(tmp_head.val)
            tmp_head = tmp_head.next
        tmp_head = A
        while tmp_head != None:
            if tmp_head.val != stk.pop():
                return 0
            tmp_head = tmp_head.next
        return 1
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
ll1 = l1
l1.next = l2
l2.next = l3
print(Solution().lPalin(ll1))
