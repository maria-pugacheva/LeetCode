class Node:
    def __init__(self, val=0):
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

    def detectCycle(self):
        """Determine if the linked list has a cycle in it."""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def testLinkedList():
    LL = LinkedList()

    # Case 1: No cycle
    LL.addAtTail(2)
    LL.addAtTail(4)
    LL.addAtTail(7)
    LL.addAtTail(3)
    LL.addAtTail(5)
    assert (LL.detectCycle() is False)

    # Case 2: Cycle exists
    LL.tail.next = LL.head
    assert (LL.detectCycle() is True)

    print('All test cases passed!')


testLinkedList()
