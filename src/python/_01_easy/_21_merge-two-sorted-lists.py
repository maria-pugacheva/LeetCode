class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        """Add a dummy node at the beginning of the list."""
        self.head = Node()
        self.tail = self.head

    def addAtTail(self, node: Node):
        self.tail.next = node
        self.tail = node

    def traverse(self):
        lst = []
        curr = self.head.next
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def mergeTwoLists(self, one: Node, two: Node):
        while one and two:
            if one.val < two.val:
                self.addAtTail(one)
                one = one.next
            else:
                self.addAtTail(two)
                two = two.next
        if one:
            self.addAtTail(one)
        if two:
            self.addAtTail(two)


def testLinkedList():
    LL1 = LinkedList()
    LL1.addAtTail(Node(1))
    LL1.addAtTail(Node(2))
    LL1.addAtTail(Node(4))
    LL1.addAtTail(Node(7))
    assert LL1.traverse() == [1, 2, 4, 7]

    LL2 = LinkedList()
    LL2.addAtTail(Node(1))
    LL2.addAtTail(Node(3))
    LL2.addAtTail(Node(4))
    assert LL2.traverse() == [1, 3, 4]

    LL3 = LinkedList()
    LL3.mergeTwoLists(LL1.head.next, LL2.head.next)
    assert LL3.traverse() == [1, 1, 2, 3, 4, 4, 7]

    print("All test cases passed!")


testLinkedList()
