class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addAtTail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def traverse(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        self.tail = self.head
        self.head = prev


def testLinkedList():
    LL = LinkedList()

    LL.reverse()
    assert (LL.traverse() == [])

    LL.addAtTail(1)
    LL.reverse()
    assert (LL.traverse() == [1])

    LL.addAtTail(2)
    LL.reverse()
    assert (LL.traverse() == [2, 1])

    LL.addAtTail(4)
    LL.reverse()
    assert (LL.traverse() == [4, 1, 2])

    print("All test cases passed!")


testLinkedList()
