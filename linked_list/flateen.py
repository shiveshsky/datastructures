def flatten(root):
    arr = []
    tmp = root
    while tmp.right is not None:
        arr.append(tmp.val)
        tmp_d = tmp
        while tmp_d is not None:
            arr.append(tmp_d.val)
            tmp_d = tmp_d.next
        tmp = tmp.right
    arr.sort()
    new_ll = None
    ptr = None
    for i in arr:
        if new_ll is not None:
            new_ll = ListNode(i)
            ptr = new_ll
        else:
            tmp = ListNode(i)
            ptr.down = tmp
            ptr = tmp
    return new_ll
