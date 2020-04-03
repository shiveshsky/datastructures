class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        return self.maxPalindrome(A)

    def countCommon(self, a, b):
        count = 0

        # loop to count coomon in the list starting
        # from node a and b
        while a is not None and b is not None:

            # increment the count for same values
            if a.val == b.val:
                count = count + 1
            else:
                break

            a = a.next
            b = b.next

        return count

    # Returns length of the longest palindrome
    # sublist in given list
    def maxPalindrome(self, head):
        result = 0
        prev = None
        curr = head

        # loop till the end of the linked list
        while curr is not None:
            # The sublist from head to current
            # reversed.
            next = curr.next
            curr.next = prev

            # check for odd length
            # palindrome by finding
            # longest common list elements
            # beginning from prev and
            # from next (We exclude curr)
            result = max(result, 2 * self.countCommon(prev, next) + 1)

            # check for even length palindrome
            # by finding longest common list elements
            # beginning from curr and from next
            result = max(result, 2 * self.countCommon(curr, next))

            # update prev and curr for next iteration
            prev = curr
            curr = next

        return result

a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(2)
a5 = ListNode(2)
a6 = ListNode(2)
a7 = ListNode(6)
a8 = ListNode(7)
a9 = ListNode(8)
a10 = ListNode(8)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a9
a9.next = a10
print(Solution().maxPalindrome(a1))

