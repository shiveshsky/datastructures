class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        tortoise = A
        hare = A

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise.val


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
# a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
# a4.next = a5

print(Solution().solve(a1))