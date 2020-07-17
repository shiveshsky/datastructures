class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        pass

    def merge(self, l, r):
        if l is None:
            return r
        if r is None:
            return l

        result = None
        if l.val < r.val:
            result = l
            result.next = self.merge(l.next, r)
        else:
            result = r
            result.next = self.merge(l, r.next)
        return result

    def merge_sort(self, head):
        if head is None:
            return
        if head.next is None:
            return head
        mid = self.get_mid(head)
        mid_next = mid.next
        mid.next = None
        l = self.merge_sort(head)
        r = self.merge_sort(mid_next)

        sort_ll = self.merge(l, r)
        return sort_ll

    def get_mid(self, head):
        tortoise = head
        hare = head
        if head is None:
            return None

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise
