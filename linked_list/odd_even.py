class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        odd_head = head
        even_head = head.next
        odd_ = odd_head
        even_ = even_head
        while (odd_ is not None and odd_.next is not None) and (even_ is not None and even_.next is not None):
            odd_.next = odd_.next.next
            odd_ = odd_.next
            even_.next = even_.next.next
            even_ = even_.next
        odd_.next = even_head
        return odd_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().oddEvenList(head)
