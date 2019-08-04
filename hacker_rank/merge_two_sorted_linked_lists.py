def newList(head1, head2):
    head1 = head1.next
    while head2.data < head1.data:
        # head1.data
        current = head2
        current.next = head1
        head1 = current
        head2 = head2.next

    # temp = head2
    # while head1:
    #     head2 = temp
    #     count = 0
    #     while head2:
    #         if head2.data <= head1.data:
    #             count += 1
    #             next_element = head1.next
    #             current_element = head2
    #             current_element.next = next_element
    #             head2 = head2.next
    #             head1.next = current_element
    #         else:
    #             head2 = None
    #             temp = temp.next
    #     for _ in range(count + 1):
    #         head1 = head1.next
    # return head1


def createNewList(head1, head2):
    head = head1 if head1.data <= head2.data else head2
    if head is head1:
        return newList(head, head2)
    else:
        return newList(head, head1)


def mergeLists(head1, head2):
    if head1 and head2:
        return createNewList(head1, head2)
    elif head1:
        return head1
    else:
        return head2


class Node:

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class LinkedList:

    def __init__(self, head):
        self.head = head


node1 = Node(3)
node2 = Node(2, node1)
node3 = Node(1, node2)
# node4 = Node(4, node3)
# node5 = Node(5, node4)

node11 = Node(6)
node22 = Node(5, node11)
node33 = Node(4, node22)
# node44 = Node(4, node33)
# node55 = Node(5, node44)

print(mergeLists(node3, None))
print(mergeLists(None, node33))
print(mergeLists(node3, node33))
