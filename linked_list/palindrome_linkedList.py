class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        if fast is not None:
            slow = slow.next
        while slow is not None and prev is not None:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
