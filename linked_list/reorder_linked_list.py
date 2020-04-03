class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middle_linked_list(self, A):
        tortoise = A
        hare = A

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise

    def reverse_linked_list(self, A):
        curr = A
        nxt = None
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        A = prev

        return A

    def reorderList(self, A):
        middle_node = self.middle_linked_list(A)
        remainin_list = middle_node.next
        middle_node.next = None
        reverse_of_rem_list = self.reverse_linked_list(remainin_list)
        tmp2 = reverse_of_rem_list
        tmp1 = A
        ans = None
        current_node = None
        flip = True
        if tmp1 is None or tmp2 is None:
            return A
        while tmp1 is not None and tmp2 is not None:
            if ans == None:
                ans = tmp1
                tmp1 = tmp1.next
                current_node = ans
            else:
                if flip:
                    current_node.next = tmp2
                    tmp2 = tmp2.next
                    flip = False
                    current_node = current_node.next
                else:
                    current_node.next = tmp1
                    tmp1 = tmp1.next
                    flip = True
                    current_node = current_node.next
        if tmp1 is not None:
            current_node.next = tmp1
        elif tmp2 is not None:
            current_node.next = tmp2
        return ans


a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(3)
# a4 = ListNode(4)
# a5 = ListNode(5)
# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
print(Solution().reorderList(a1))
