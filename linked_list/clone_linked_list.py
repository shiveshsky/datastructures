class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


def clonelist(A):
    tmpA = A
    newLL = None
    address_hash = {}
    current_ptr = None
    while tmpA is not None:
        if newLL is None:
            newLL = ListNode(tmpA.val)
            current_ptr = newLL
            address_hash[tmpA] = newLL
        else:
            newNode = ListNode(tmpA.val)
            current_ptr.next = newNode
            current_ptr = current_ptr.next
            address_hash[tmpA] = current_ptr
        tmpA = tmpA.next
    tmpA = A
    current_ptr = newLL
    while tmpA is not None:
        current_ptr.random = address_hash.get(tmpA.random)
        tmpA = tmpA.next
        current_ptr = current_ptr.next
    return newLL

