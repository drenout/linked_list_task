# Enter your code here. Read input from STDIN. Print output to STDOUT

# !/usr/bin/env python

class Node:
    def __init__(self, node_value):
        self.value = node_value
        self.next = None

    # [2]->[4]->[1]->[2]
    # [1]->[4]
    def __str__(self):
        if not self.next:
            return '[{}]'.format(str(self.value))
        else:
            return '[{}]->{}'.format(str(self.value),str(self.next))

def insert_in_sorted_list(head, node):
    if node.value <= head.value:
        node.next = head
        return node
    curr_node = head
    next_node = head.next
    while next_node:
        if (node.value >= curr_node.value) and (node.value <= next_node.value):
            curr_node.next = node
            node.next = next_node
            return head
        curr_node = next_node
        next_node = next_node.next
    curr_node.next = node
    node.next = None
    return head

def delete_is_used(head):
    del head.is_used
    while head.next:
        del head.next.is_used
        head = head.next

def find_delete_sort(head, key):
    if not isinstance(head, Node) or not isinstance(key, int):
        print('Please pass a (Node, int) type of objects to the function')
        exit()
    # Init new head for sorted+deleted list
    new_head = None
    while True:
        # Check for looped linked list
        if hasattr(head, 'is_used'):
            return new_head
        # Marking node as already checked
        head.__setattr__('is_used', True)
        if head.value != key:
            new_head = head
            break
        if head.next:
            head = head.next
        # Found last element
        else:
            return new_head

    head = new_head.next
    # Clearing next reference for the new head
    new_head.next = None
    print(new_head)
    try:
        int(new_head.value)
    except ValueError:
        print('Non-integer value was found, exiting')
        return new_head

    while True:
        if hasattr(head, 'is_used'):
            break
        if head:
            head.__setattr__('is_used', True)
            next_head = head.next
            print('New element:',head.value)
            try:
                int(head.value)
            except ValueError:
                print('Non-integer value was found, exiting')
                return new_head
            if head.value != key:
                new_head = insert_in_sorted_list(new_head, head)
            print(new_head)
            head = next_head
        # Already inserted the last element
        else:
            break
    delete_is_used(new_head)
    return new_head


if __name__ == '__main__':
    a = Node(17)
    b = Node(17)
    c = Node(53)
    d = Node(6546879687)
    e = Node(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = a
    find_delete_sort(a, 17)

