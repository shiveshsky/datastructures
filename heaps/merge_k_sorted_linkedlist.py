# Definition for singly-linked list.
from heapq import heapify, heappop, heappush
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Ele:
    def __init__(self, ele, ind):
        self.ele = ele
        self.ind = ind

    def __lt__(self, other):
        if self.ele.val < other.ele.val:
            return True
        return False


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minhp = []
        heapify(minhp)
        i = 0
        head = None
        ptr = None
        while len(minhp) < len(lists):
            ll = lists[i]
            heappush(minhp, Ele(ll, i))
            i += 1
        while len(minhp) > 0:
            el = heappop(minhp)
            if head is None:
                head = ListNode(el.ele.val)
                ptr = head
                if el.ele.next:
                    heappush(minhp, Ele(el.ele.next, el.ind))
            else:
                tmp = ListNode(el.ele.val)
                ptr.next = tmp
                ptr = ptr.next
                if el.ele.next:
                    heappush(minhp, Ele(el.ele.next, el.ind))
        return head


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    Solution().mergeKLists([l1, l2, l3])
