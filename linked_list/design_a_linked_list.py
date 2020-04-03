class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
length = 0


def insert_node(position, value):
    global head
    global length
    if position>length+1:
        return
    if head is None and position == 1:
        head = ListNode(value)
        length +=1
    elif head is not None:
        tmp = head
        while position > 2 and tmp.next is not None:
            tmp = tmp.next
            position -= 1
        newnode = ListNode(value)

        if position==1:
            newnode.next = head
            head = newnode
        else:
            newnode.next = tmp.next
            tmp.next = newnode
        length += 1


def delete_node(position):
    global head
    global length
    tmp = head
    prev = None
    if position > length:
        return
    while position > 1 and tmp.next is not None:
        prev = tmp
        tmp = tmp.next
        position -= 1
    if prev is None:
        length -= 1
        head = tmp.next
    else:
        length -= 1
        prev.next = tmp.next


def print_ll():
    global head
    tmp = head
    ans = []
    while tmp is not None:
        # print(tmp.val, end=" ")
        ans.append(str(tmp.val))
        tmp = tmp.next
    print(" ".join(ans))


# if __name__ == '__main__':
#     insert_node(1, 23)
#     insert_node(2, 24)
#     insert_node(3, 25)
#     insert_node(1, 1)
#     insert_node(2, 2)
#     insert_node(3, 3)
#     insert_node(4, 4)
#     insert_node(7, 7)
#     insert_node(8, 8)
#     print_ll()
#     delete_node(1)
#     print_ll()

def main():
    cases, position, value = 0, 0, 0
    cases = int(input())
    while (cases > 0):
        inp = input().split()
        ch = inp[0]
        if ch == 'i':
            position = int(inp[1])
            value = int(inp[2])
            insert_node(position, value)
        elif ch == 'd':
            position = int(inp[1])
            delete_node(position)
        elif ch == 'p':
            print_ll()
        else:
            print("Check your input")
        cases -= 1

if __name__ == '__main__':
    main()
